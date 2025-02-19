import unittest

from src.droptask import services, repository, exceptions


class TestSortService(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()

    def tearDown(self):
        repository.reset_all_tasks()

    def test_sort_by_priority(self):
        tasks = services.sort_tasks("priority")
        correct_order = [1, 1, 2, 3, 3]
        for i, task in enumerate(tasks):
            self.assertEqual(task.priority.value, correct_order[i])

    def test_sort_by_priority_desc(self):
        tasks = services.sort_tasks("priority", True)
        correct_order = [3, 3, 2, 1, 1]
        for i, task in enumerate(tasks):
            self.assertEqual(task.priority.value, correct_order[i])

    def test_sort_by_is_done(self):
        tasks = services.sort_tasks("is_done")
        correct_order = [0, 0, 0, 1, 1]
        for i, task in enumerate(tasks):
            self.assertEqual(task.is_done, correct_order[i])

    def test_sort_by_is_done_desc(self):
        tasks = services.sort_tasks("is_done", True)
        correct_order = [1, 1, 0, 0, 0]
        for i, task in enumerate(tasks):
            self.assertEqual(task.is_done, correct_order[i])

    def test_sort_by_due(self):
        tasks = services.sort_tasks("due")
        correct_order = [1, 2, 3, 4, 5]
        for i, task in enumerate(tasks):
            self.assertEqual(task.task_id, correct_order[i])

    def test_sort_by_due_desc(self):
        tasks = services.sort_tasks("due", True)
        correct_order = [5, 4, 3, 2, 1]
        for i, task in enumerate(tasks):
            self.assertEqual(task.task_id, correct_order[i])

    def test_sort_invalid_fields(self):
        with self.assertRaises(exceptions.InvalidField):
            services.sort_tasks("hello")


if __name__ == '__main__':
    unittest.main()
