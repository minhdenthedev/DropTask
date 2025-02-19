import random
from datetime import datetime, timedelta

# Generate random task names
task_names = [
    "Finish report", "Buy groceries", "Read a book", "Workout",
    "Schedule meeting", "Call client", "Pay bills", "Write blog post",
    "Review PR", "Plan weekend trip"
]

# Random priority levels
priorities = ["High", "Medium", "Low"]

# Random collections (task categories)
collections = ["Work", "Personal", "Health", "Finance", "Learning"]

# Generate fake tasks
fake_db = {}

for i in range(10):  # Generate 10 tasks
    task_id = i  # Unique task ID
    task_name = random.choice(task_names)
    due_date = datetime.now() + timedelta(days=random.randint(1, 30))  # Random future due date
    priority = random.choice(priorities)
    collection = random.choice(collections)
    is_done = random.choice([True, False])

    fake_db[task_id] = {
        "name": task_name,
        "due": str(due_date.strftime("%Y-%m-%d %H:%M:%S")),  # Convert to string format
        "priority": priority,
        "collection": collection,
        "is_done": is_done
    }

print(fake_db)
