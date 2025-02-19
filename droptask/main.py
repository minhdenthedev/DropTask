from droptask.cli import cli
from droptask import services

if __name__ == '__main__':
    services.update_task(3, "name:hello bitches")
    print(services.get_all_tasks())
