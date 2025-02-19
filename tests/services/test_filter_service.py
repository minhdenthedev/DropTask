import unittest

from src.droptask import repository, services
from src.droptask.exceptions import InvalidField


class TestFilterService(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()

    def tearDown(self):
        repository.reset_all_tasks()

    def test_filter(self):
        filter_dict = {
            "collection": "My Tasks",
            "priority": 3,
            "is_done": False
        }
        tasks = services.filter_tasks_on_categories(filter_dict)
        self.assertEqual(tasks[0].task_id, 1)

    def test_filter_invalid_field(self):
        with self.assertRaises(InvalidField):
            filter_dict = {
                "name": "1",
                "collection": "My Tasks",
                "priority": "low",
                "is_done": False
            }
            services.filter_tasks_on_categories(filter_dict)


if __name__ == '__main__':
    unittest.main()
