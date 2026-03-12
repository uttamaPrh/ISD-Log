from typing import List
from tasks import Task


class TaskList:
    """Manage a collection of Task objects."""

    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the list."""
        self.tasks.append(task)

    def remove_task(self, index: int) -> None:
        """Remove a task by index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid index")

    def get_task(self, index: int) -> Task | None:
        """Return a task by index if it exists."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks."""
        return self.tasks

    def display_tasks(self) -> None:
        """Print all tasks with their list index."""
        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")

    def __str__(self) -> str:
        return f"TaskList with {len(self.tasks)} tasks"
