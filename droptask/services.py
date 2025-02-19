from droptask.models import TaskModel, Priority
from datetime import datetime
from droptask import repository


def add_task(task_name: str, due_str: str = None, priority: Priority = Priority.MEDIUM,
             collection: str = "My Tasks"):
    due = datetime.strptime(due_str, "%Y-%m-%d %H:%M:%S") if due_str else ""
    task = TaskModel(
        task_id=repository.get_latest_id() + 1,
        task_name=task_name,
        due=due,
        priority=priority,
        collection=collection,
        is_done=False
    )
    repository.insert_task(task)


def remove_task(task_id: int):
    repository.delete_task_by_id(task_id)


def update_task(task_id: int, key_value_str: str):
    key_value = key_value_str.split(":")
    key = key_value[0]
    value = key_value[1]
    repository.update_task_by_id(task_id, key, value)


def get_task(task_id: int):
    return repository.get_task_by_id(task_id)





def get_all_tasks():
    return repository.get_all_tasks()
