from typing import Optional, List, Dict
import sqlite3
from src.droptask.models import TaskModel, Priority
from src.droptask import utils
from datetime import datetime, timedelta

from src.droptask import exceptions

DB_PATH = "/home/m1nhd3n/Works/SideProjects/DropTask/data/tasks.db"


def init_test_data():
    cnx = sqlite3.connect(DB_PATH)
    try:
        cur = cnx.cursor()
        task_ids = [1, 2, 3, 4, 5]
        task_names = ["1", '2', '3', '4', '5']
        task_due = [utils.parse_dt_to_str(datetime.now() + timedelta(days=i)) for i in range(1, 6)]
        task_priorities = [3, 2, 3, 1, 1]
        task_collection = ["My Tasks", "Works", "Classroom", "My Tasks", "My Tasks"]
        task_is_done = [False, False, True, False, True]
        query = """
                    INSERT INTO tasks (task_id, name, due, priority, collection, is_done)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """
        for i in range(5):
            cur.execute(query, (task_ids[i],
                                task_names[i],
                                task_due[i],
                                task_priorities[i],
                                task_collection[i],
                                task_is_done[i]))
        cnx.commit()
    except sqlite3.OperationalError:
        cnx.commit()
    finally:
        cnx.close()


def init_database() -> bool:
    cnx = sqlite3.connect(DB_PATH)  # Replace with your DB file
    cur = cnx.cursor()

    # Check if the table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
    table_exists = cur.fetchone() is not None  # Returns True if the table exists

    if table_exists:
        cnx.close()
        return True

    # Create table and index if not exists
    create_query = """
    CREATE TABLE IF NOT EXISTS tasks(
        task_id INTEGER PRIMARY KEY, 
        name TEXT, 
        due TEXT, 
        priority INTEGER, 
        collection TEXT, 
        is_done INTEGER
    )
    """
    index_query = """
    CREATE UNIQUE INDEX IF NOT EXISTS task_id_idx ON tasks (task_id)
    """

    try:
        cur.execute(create_query)
        cur.execute(index_query)
        cnx.commit()
        return True
    except sqlite3.ProgrammingError:
        cnx.rollback()
        return False
    finally:
        cnx.close()


# Example usage
init_database()


def insert_task(task: TaskModel):
    """Insert a new task into the database."""

    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    try:
        query = """
        INSERT INTO tasks (task_id, name, due, priority, collection, is_done)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cur.execute(query,
                    (task.task_id, task.task_name,
                     utils.parse_dt_to_str(task.due), task.priority.value, task.collection, task.is_done))
        cnx.commit()
    except sqlite3.IntegrityError:
        raise exceptions.TaskExists(task.task_id)
    finally:
        cnx.close()


def delete_task_by_id(task_id: int):
    """Delete a task by ID."""
    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    try:
        cur.execute("DELETE FROM tasks WHERE task_id = ?",
                    (task_id,))
        # Shift id forward for ids in range(task_id + 1, latest_id)
        latest_id = get_latest_id()
        for i in range(task_id, latest_id):
            cur.execute("UPDATE tasks SET task_id = ? WHERE task_id = ?",
                        (i, i + 1))
        if cur.rowcount == 0:
            raise exceptions.TaskNotFound(task_id)
        cnx.commit()
    finally:
        cnx.close()


def update_task_by_id(task_id: int, key: str, value: str):
    """Update a specific field of a task by ID."""
    cnx = sqlite3.connect(DB_PATH)
    try:
        cur = cnx.cursor()

        query = f"UPDATE tasks SET {key} = ? WHERE task_id = ?"
        cur.execute(query, (value, task_id))
        if cur.rowcount == 0:
            raise exceptions.TaskNotFound(task_id)
        cnx.commit()
    finally:
        cnx.close()


def get_all_tasks() -> List[TaskModel]:
    """Retrieve all tasks from the database."""
    cnx = sqlite3.connect(DB_PATH)
    try:
        cur = cnx.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()

        return [TaskModel(
            task_id=int(row[0]),
            task_name=row[1],
            due=utils.parse_str_to_dt(row[2]),
            priority=Priority(row[3]),
            collection=row[4],
            is_done=bool(row[5])
        ) for row in tasks
        ]
    finally:
        cnx.close()


def get_task_by_id(task_id: int) -> Optional[TaskModel]:
    """Retrieve a task by ID."""
    cnx = sqlite3.connect(DB_PATH)
    try:
        cur = cnx.cursor()
        cur.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
        row = cur.fetchone()
        if row:
            return TaskModel(
                task_id=int(row[0]),
                task_name=row[1],
                due=utils.parse_str_to_dt(row[2]),
                priority=Priority(row[3]),
                collection=row[4],
                is_done=bool(row[5])
            )
        else:
            raise exceptions.TaskNotFound(task_id)

    except sqlite3.InternalError:
        raise RuntimeError("Something wrong, try again later")
    finally:
        cnx.close()


def get_latest_id() -> int:
    """Retrieve the latest task ID based on insertion order."""
    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    cur.execute("SELECT task_id FROM tasks ORDER BY ROWID DESC LIMIT 1")
    row = cur.fetchone()
    if not row:
        return 0
    cnx.close()
    return int(row[0]) if row else None


def reset_all_tasks():
    cnx = sqlite3.connect(DB_PATH)
    try:
        cur = cnx.cursor()
        cur.execute("DROP TABLE tasks")
        cnx.commit()
    except sqlite3.OperationalError as e:
        raise e
    finally:
        cnx.close()

    init_database()


def filter_task(filter_dict: Dict[str, str]) -> List[TaskModel]:
    cnx = sqlite3.connect(DB_PATH)
    query = """
    SELECT * FROM tasks WHERE
    """
    try:
        n = len(filter_dict)
        cur = cnx.cursor()
        if filter_dict is None:
            raise ValueError("Filter dict is None.")
        for i, key in enumerate(filter_dict.keys()):
            if i == n - 1:
                query += f"{key} = ?"
            else:
                query += f"{key} = ? AND "
        data = []
        for value in filter_dict.values():
            data.append(value)
        cur.execute(query, data)
        rows = cur.fetchall()
        return [
            TaskModel(
                task_id=int(row[0]),
                task_name=row[1],
                due=utils.parse_str_to_dt(row[2]),
                priority=Priority(row[3]),
                collection=row[4],
                is_done=bool(row[5])
            ) for row in rows]
    except sqlite3.OperationalError as e:
        raise e
    finally:
        cnx.close()


def search_name(name: str):
    cnx = sqlite3.connect(DB_PATH)
    query = """
        SELECT * FROM tasks WHERE name LIKE ?
        """
    try:
        cur = cnx.cursor()
        cur.execute(query, ('%' + name + '%'))
        rows = cur.fetchall()
        return [
            TaskModel(
                task_id=int(row[0]),
                task_name=row[1],
                due=utils.parse_str_to_dt(row[2]),
                priority=Priority(row[3]),
                collection=row[4],
                is_done=bool(row[5])
            ) for row in rows]
    except sqlite3.OperationalError as e:
        raise e
    finally:
        cnx.close()


def sort_tasks(by: str, desc: bool = False):
    cnx = sqlite3.connect(DB_PATH)
    query = f"""
            SELECT * FROM tasks ORDER BY {by} {"DESC" if desc else "ASC"}
            """
    try:
        cur = cnx.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return [
            TaskModel(
                task_id=int(row[0]),
                task_name=row[1],
                due=utils.parse_str_to_dt(row[2]),
                priority=Priority(row[3]),
                collection=row[4],
                is_done=bool(row[5])
            ) for row in rows]
    except sqlite3.OperationalError as e:
        raise e
    finally:
        cnx.close()
