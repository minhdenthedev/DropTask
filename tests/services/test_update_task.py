import unittest
from datetime import datetime

from src.droptask import repository, services, exceptions
from src.droptask.models import TaskModel


class TestUpdateTaskService(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()

    def tearDown(self):
        repository.reset_all_tasks()

    def test_update_normal(self):
        services.update_task(1, "name:hello")
        self.assertEqual(0, 0)

    def test_update_invalid_id(self):
        with self.assertRaises(exceptions.TaskNotFound):
            services.update_task(999, "name:hello")

    def test_update_invalid_key(self):
        with self.assertRaises(exceptions.InvalidField):
            services.update_task(1, "haha:hehe")

    def test_mark_as_done(self):
        services.mark_status(1, 1)
        self.assertEqual(0, 0)

    def test_mark_as_done_invalid_key(self):
        with self.assertRaises(exceptions.InvalidStatus):
            services.mark_status(1, 999)

    def test_mark_as_done_invalid_task_id(self):
        with self.assertRaises(exceptions.TaskNotFound):
            services.mark_status(999, 1)


if __name__ == '__main__':
    unittest.main()
