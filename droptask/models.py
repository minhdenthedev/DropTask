from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskModel:
    def __init__(self,
                 task_id: int,
                 task_name: str,
                 due: datetime | str,
                 priority: Priority,
                 collection: str,
                 is_done: bool):
        self.task_id: int = task_id
        self.task_name: str = task_name
        self.due: datetime = due
        self.priority: Priority = priority
        self.collection: str = collection
        self.is_done: bool = is_done
