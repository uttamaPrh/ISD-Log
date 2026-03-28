from tasks import Task

class TaskList:
    def __init__(self, list_owner: str):
        self.list_owner = list_owner
        self.task_items = []

    def add_task(self, task: Task):
        self.task_items.append(task)

    def remove_task(self, task_index: int):
        if 0 <= task_index < len(self.task_items):
            self.task_items.pop(task_index)
        else:
            print("Task not found")

    def get_task(self, task_index: int):
        if 0 <= task_index < len(self.task_items):
            return self.task_items[task_index]
        return None

    @property
    def uncompleted_tasks(self):
        return [task for task in self.task_items if not task.is_done]

    def view_tasks(self):
        print("The following tasks are still to be done:")

        if not self.uncompleted_tasks:
            print("No remaining tasks")
            return

        for task in self.uncompleted_tasks:
            task_index = self.task_items.index(task)
            print(f"{task_index}: {task}")