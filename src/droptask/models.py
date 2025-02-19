from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TaskModel:
    def __init__(self,
                 task_id: int,
                 task_name: str,
                 due: datetime = None,
                 priority: Priority = Priority.MEDIUM,
                 collection: str = "My Tasks",
                 is_done: bool = False):
        self.task_id: int = task_id
        self.task_name: str = task_name
        self.due: datetime = due
        self.priority: Priority = priority
        self.collection: str = collection
        self.is_done: bool = is_done

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "name": self.task_name,
            "due": self.due,
            "priority": self.priority,
            "collection": self.collection,
            "is_done": self.is_done
        }