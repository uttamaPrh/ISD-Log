from tasks import Task
import datetime


class TaskList:
    def __init__(self, owner: str):
        self.owner = owner
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        del self.tasks[ix]

    def view_tasks(self) -> None:
        print(f"Task list for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            print(f"{ix}: {task}")

    def view_overdue_tasks(self) -> None:
        now = datetime.datetime.now()
        overdue_found = False
        print(f"Overdue tasks for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            if task.date_due < now and not task.completed:
                print(f"{ix}: {task}")
                overdue_found = True
        if not overdue_found:
            print("No overdue tasks found.")
