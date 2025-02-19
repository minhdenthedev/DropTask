import unittest
from datetime import datetime

from src.droptask import repository, exceptions
from src.droptask.models import TaskModel


class TestGetById(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()

    def tearDown(self):
        repository.reset_all_tasks()

    def test_get_by_id(self):
        task = repository.get_task_by_id(1)
        self.assertIsInstance(task, TaskModel)
        repository.reset_all_tasks()

    def test_get_by_invalid_id(self):
        with self.assertRaises(exceptions.TaskNotFound):
            repository.get_task_by_id(999)


if __name__ == '__main__':
    unittest.main()
