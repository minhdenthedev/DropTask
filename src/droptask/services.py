from typing import List, Dict

from src.droptask.models import TaskModel, Priority
from src.droptask import repository, utils, exceptions


def add_task(task_name: str, due_str: str = None, priority: Priority = Priority.MEDIUM,
             collection: str = "My Tasks"):
    due = utils.parse_str_to_dt(due_str)
    if utils.is_dt_past(due):
        raise exceptions.InvalidDatetime()

    task = TaskModel(
        task_id=repository.get_latest_id() + 1,
        task_name=task_name,
        due=due,
        priority=priority,
        collection=collection,
        is_done=False
    )
    repository.insert_task(task)
    return task


def remove_task(task_id: int):
    repository.delete_task_by_id(task_id)


def update_task(task_id: int, key_value_str: str):
    key_value = key_value_str.split(":")
    key = key_value[0]
    value = key_value[1]
    valid_columns = {"name", "due", "priority", "collection", "is_done"}
    if key not in valid_columns:
        raise exceptions.InvalidField(key)
    if key == "due":
        if utils.is_dt_past(utils.parse_str_to_dt(key_value_str)):
            raise exceptions.InvalidDatetime()
    repository.update_task_by_id(task_id, key, value)


def get_task(task_id: int) -> TaskModel:
    return repository.get_task_by_id(task_id)


def get_all_tasks() -> List[TaskModel]:
    return repository.get_all_tasks()


def mark_status(task_id: int, status: int):
    if status not in [0, 1]:
        raise exceptions.InvalidStatus(status)
    repository.update_task_by_id(task_id, "is_done", str(status))


def filter_tasks_on_categories(filter_dict: Dict[str, str]):
    valid_columns = ["priority", "collection", "is_done"]
    for key in filter_dict.keys():
        if key not in valid_columns:
            raise exceptions.InvalidField(key, valid_columns)

    return repository.filter_task(filter_dict)


def search_name(name: str):
    return repository.search_name(name)


def sort_tasks(by: str, desc: bool = False):
    valid_cols = ["task_id", "name", "due", "priority", "collection", "is_done"]
    if by not in valid_cols:
        raise exceptions.InvalidField(by, valid_cols)
    return repository.sort_tasks(by, desc)