import unittest
from datetime import datetime

from src.droptask import repository, exceptions
from src.droptask.models import TaskModel


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        repository.reset_all_tasks()
        for i in range(5):
            new_task = TaskModel(
                task_id=i,
                task_name="test",
                due=datetime(2025, 3, 2)
            )
            repository.insert_task(new_task)

    def tearDown(self):
        repository.reset_all_tasks()

    def test_delete_task(self):
        repository.delete_task_by_id(1)
        latest_id = repository.get_latest_id()
        self.assertEqual(latest_id, 3)
        tasks = repository.get_all_tasks()
        for i in range(4):
            self.assertEqual(tasks[i].task_id, i)

    def test_delete_by_invalid_id(self):
        with self.assertRaises(exceptions.TaskNotFound):
            repository.delete_task_by_id(999)


if __name__ == '__main__':
    unittest.main()
