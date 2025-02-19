import argparse
from src.droptask import services


def cli():
    parser = argparse.ArgumentParser(description="Cloud-based CLI To-Do App using Dropbox")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="Task description")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")

    # Mark task as done
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_id", type=int, help="Task ID to mark as completed")

    # Remove task
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("task_id", type=int, help="Task ID to remove")

    args = parser.parse_args()

    if args.command == "add":
        services.add_task(args.task)
    elif args.command == "list":
        print("list")
    elif args.command == "done":
        print(f"done {args}")
    elif args.command == "remove":
        services.remove_task(args.task_id)

    tasks = services.get_all_tasks()
    for task in tasks:
        print(task)
