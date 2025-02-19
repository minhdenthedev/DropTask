from typing import List


class InvalidDatetimeFormat(Exception):
    """Exception raised for invalid datetime format."""

    def __init__(self,
                 received_dt: str,
                 message="Invalid datetime format. Expected format: DD-MM-YYYY HH:MM:SS"):
        message += f". Received: {received_dt}"
        super().__init__(message)


class InvalidDatetime(Exception):
    def __init__(self, message="Can not set due to the past."):
        super().__init__(message)


class TaskNotFound(Exception):
    def __init__(self, task_id_not_found: int):
        message = f"Task with task_id={task_id_not_found} is not found."
        super().__init__(message)


class TaskExists(Exception):
    def __init__(self, task_id: int):
        message = f"Task with task_id={task_id} exists."
        super().__init__(message)


class InvalidStatus(Exception):
    def __init__(self, invalid_value: int):
        message = f"Task's status must be 0 (not done) or 1 (done). Received: {invalid_value}"
        super().__init__(message)


class InvalidField(Exception):
    def __init__(self, invalid_value: str, expected_fields: List[str] = None):
        if expected_fields is None:
            message = f"Valid fields: ['name', 'due', 'priority', 'collection']. Received: {invalid_value}"
        else:
            message = f"Valid fields: {expected_fields}. Received: {invalid_value}"
        super().__init__(message)
