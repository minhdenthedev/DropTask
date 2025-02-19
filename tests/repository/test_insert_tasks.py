import unittest
from src.droptask import repository
from src.droptask.models import TaskModel
from datetime import datetime


class TestInsertTasks(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()

    def tearDown(self):
        repository.reset_all_tasks()

    def test_insert(self):
        new_task = TaskModel(
            task_id=6,
            task_name="test",
            due=datetime(2025, 3, 2)
        )
        repository.insert_task(new_task)
        task = repository.get_task_by_id(6)
        self.assertEqual(task.task_id, new_task.task_id)
        self.assertEqual(task.task_name, new_task.task_name)
        self.assertEqual(task.due, new_task.due)
        self.assertEqual(task.priority, new_task.priority)
        self.assertEqual(task.collection, new_task.collection)
        self.assertEqual(task.is_done, new_task.is_done)


if __name__ == '__main__':
    unittest.main()
