import unittest

from src.droptask import repository


class TestResetTasks(unittest.TestCase):
    def test_reset_all_tasks(self):
        repository.reset_all_tasks()
        tasks = repository.get_all_tasks()
        self.assertEqual(len(tasks), 0)


if __name__ == '__main__':
    unittest.main()
