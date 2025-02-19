from typing import Dict, Optional
import sqlite3
from droptask.models import TaskModel

DB_PATH = "/home/m1nhd3n/Works/SideProjects/DropTask/data/tasks.db"


def init_database():
    cnx = sqlite3.connect(DB_PATH)  # Replace with your DB file
    cur = cnx.cursor()

    # Check if the table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
    table_exists = cur.fetchone() is not None  # Returns True if the table exists

    if table_exists:
        print("Database already initialized.")
        cnx.close()
        return

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
        print("Database initialized successfully.")
    except sqlite3.ProgrammingError:
        cnx.rollback()
        print("Error: More than one SQL is being executed")
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
                     task.due, task.priority.value, task.collection, task.is_done))
        cnx.commit()
    except sqlite3.IntegrityError:
        raise KeyError(f"Task with id={task.task_id} already exists.")
    finally:
        cnx.close()


def delete_task_by_id(task_id: int):
    """Delete a task by ID."""
    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    try:
        cur.execute("DELETE FROM tasks WHERE task_id = ?",
                    (task_id,))
        if cur.rowcount == 0:
            raise KeyError(f"Task with id={task_id} does not exist.")
        cnx.commit()
    finally:
        cnx.close()


def update_task_by_id(task_id: int, key: str, value: str):
    """Update a specific field of a task by ID."""
    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    try:
        # Ensure the column exists to prevent SQL injection
        valid_columns = {"name", "due", "priority", "collection", "is_done"}
        if key not in valid_columns:
            raise ValueError(f"Invalid column: {key}")

        query = f"UPDATE tasks SET {key} = ? WHERE task_id = ?"
        cur.execute(query, (value, task_id))
        if cur.rowcount == 0:
            raise KeyError(f"Task with id={task_id} does not exist.")
        cnx.commit()
    finally:
        cnx.close()


def get_all_tasks():
    """Retrieve all tasks from the database."""
    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cnx.close()
    return tasks


def get_task_by_id(task_id: int) -> Optional[TaskModel]:
    """Retrieve a task by ID."""
    cnx = sqlite3.connect(DB_PATH)
    cur = cnx.cursor()
    cur.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
    row = cur.fetchone()
    cnx.close()
    if row:
        return TaskModel(*row)
    return None


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
