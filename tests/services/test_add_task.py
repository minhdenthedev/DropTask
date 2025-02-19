import unittest
from datetime import datetime

from src.droptask import repository, services
from src.droptask.exceptions import InvalidDatetime
from src.droptask.models import TaskModel


class TestAddTaskService(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()

    def tearDown(self):
        repository.reset_all_tasks()

    def test_add_task_normal(self):
        services.add_task("hello", "29-03-2025")
        self.assertEqual(1, 1)

    def test_add_task_in_past(self):
        with self.assertRaises(InvalidDatetime):
            services.add_task("hello", "01-01-2023")


if __name__ == '__main__':
    unittest.main()
