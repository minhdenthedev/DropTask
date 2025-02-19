import unittest

from src.droptask import repository, utils
from src.droptask.models import TaskModel, Priority
from datetime import datetime


class TestUpdateTask(unittest.TestCase):
    def setUp(self):
        repository.init_test_data()
        self.valid_columns = ["name", "due", "priority", "collection", "is_done"]

    def tearDown(self):
        repository.reset_all_tasks()

    def test_update_task(self):
        new_name = "renamed"
        new_due = datetime.now()
        new_prior = Priority.HIGH.value
        new_col = "Test Collection"
        new_status = True
        new_values = [new_name, utils.parse_dt_to_str(new_due), new_prior, new_col, new_status]
        for i in range(len(self.valid_columns)):
            repository.update_task_by_id(1, self.valid_columns[i], new_values[i])
        updated_task = repository.get_task_by_id(1)
        self.assertEqual(updated_task.task_name, new_name)
        self.assertEqual(utils.parse_dt_to_str(updated_task.due), utils.parse_dt_to_str(new_due))
        self.assertEqual(updated_task.priority, Priority(new_prior))
        self.assertEqual(updated_task.collection, new_col)
        self.assertEqual(updated_task.is_done, new_status)


if __name__ == '__main__':
    unittest.main()
