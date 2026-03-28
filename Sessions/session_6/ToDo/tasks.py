import datetime

class Task:
    def __init__(self, task_title: str, task_note: str, deadline: datetime.date):
        self.task_title = task_title
        self.task_note = task_note
        self.deadline = deadline
        self.is_done = False

    def mark_completed(self):
        self.is_done = True

    def __str__(self):
        status = "✓" if self.is_done else "✗"
        return f"{self.task_title} | Due: {self.deadline} | {status}"


class RecurringTask(Task):
    def __init__(self, task_title, task_note, deadline, repeat_gap):
        super().__init__(task_title, task_note, deadline)
        self.repeat_gap = repeat_gap

    def mark_completed(self):
        # Move to next due date instead of finishing
        self.deadline += self.repeat_gap

    def __str__(self):
        return f"{self.task_title} (Recurring) | Due: {self.deadline}"