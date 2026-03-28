# Portfolio Log

## Task : Portfolio Exercise 1

Add a description attribute to the `Task` class. This is optional for users when creating a task.

- Added `description` to `Task.__init__`
- Added `change_description()` to update it
- Updated `__str__` to display it
- Updated edit flow in `main()` so description can be changed in choice `4`

```python
# tasks.py
import datetime


class Task:
    def __init__(self, title, date_due, description=None):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due
        self.description = description

    def change_title(self, new_title):
        self.title = new_title

    def change_date_due(self, date_due):
        self.date_due = date_due

    def mark_completed(self):
        self.completed = True

    def change_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return (
            f"{self.title} (created: {self.date_created}, due: {self.date_due}, "
            f"completed: {self.completed}, description: {self.description})"
        )
```

```python
# tasklist.py
from tasks import Task


class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        print(f"Task list for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            print(f"{ix}: {task}")
```

```python
# main.py
from tasklist import TaskList
from tasks import Task
import datetime


def propagate_task_list(task_list):
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    return task_list


def main():
    task_list = TaskList("Uttam Pradhan")
    task_list = propagate_task_list(task_list)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Complete a task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter a task: ")
            description_input = input("Enter a description (optional): ").strip()
            description = description_input if description_input else None
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            task = Task(title, date_object, description)
            task_list.add_task(task)
        elif choice == "2":
            task_list.view_tasks()
        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
        elif choice == "4":
            ix = int(input("Enter the index of the task to edit: "))
            edit_choice = input("What would you like to edit? (title/due date/description): ")
            if edit_choice == "title":
                title = input("Enter a new title: ")
                task_list.tasks[ix].change_title(title)
            elif edit_choice == "due date":
                input_date = input("Enter a new due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task_list.tasks[ix].change_date_due(date_object)
            elif edit_choice == "description":
                description_input = input("Enter a new description (leave blank to clear): ").strip()
                description = description_input if description_input else None
                task_list.tasks[ix].change_description(description)
            else:
                print("Invalid choice.")
        elif choice == "5":
            ix = int(input("Enter the index of the task to complete: "))
            task_list.tasks[ix].mark_completed()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Portfolio/exercise_1/src/main.py"
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Quit
Enter your choice: 1
Enter a task: Java
Enter a description (optional): Qwerty
Enter a due date (YYYY-MM-DD): 2026-03-30
Enter your choice: 2
Task list for Uttam Pradhan:
0: Buy groceries (...)
1: Do laundry (...)
2: Clean room (...)
3: Do homework (...)
4: Java (... description: Qwerty)
```

## Task : Portfolio Exercise 2

Add a method to `TaskList` that allows the user to view all overdue tasks.

- Added `view_overdue_tasks()` in `tasklist.py`
- Added menu option in `main.py` to call it

```python
# tasks.py
import datetime
from typing import Optional


class Task:

    def __init__(
        self,
        title: str,
        date_due: datetime.datetime,
        description: Optional[str] = None,
    ):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due
        self.description = description

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def mark_completed(self) -> None:
        self.completed = True

    def change_description(self, new_description: Optional[str]) -> None:
        self.description = new_description

    def __str__(self) -> str:
        return (
            f"{self.title} (created: {self.date_created}, due: {self.date_due}, "
            f"completed: {self.completed}, description: {self.description})"
        )
```

```python
# tasklist.py
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
```

```python
# main.py
from tasklist import TaskList
from tasks import Task
import datetime
from typing import Optional


def parse_date(date_value: str) -> Optional[datetime.datetime]:
    try:
        return datetime.datetime.strptime(date_value, "%Y-%m-%d")
    except ValueError:
        return None


def parse_index(index_value: str, max_size: int) -> Optional[int]:
    try:
        index = int(index_value)
    except ValueError:
        return None
    if 0 <= index < max_size:
        return index
    return None


def propagate_task_list(task_list: TaskList) -> TaskList:
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
    return task_list


def main() -> None:
    task_list = TaskList("Uttam Pradhan")
    task_list = propagate_task_list(task_list)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Complete a task")
        print("6. View overdue tasks")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "6":
            task_list.view_overdue_tasks()
        elif choice == "7":
            break
        # Other choices are implemented in source file.


if __name__ == "__main__":
    main()
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Portfolio/exercise_2/src/main.py"
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. View overdue tasks
7. Quit
Enter your choice: 6
Overdue tasks for Uttam Pradhan:
0: Buy groceries (...)
2: Clean room (...)
```

## Task : Portfolio Exercise 3

At minimum, add:
- A new class called `User`
- A new class called `Owner` inheriting from `User`
- `TaskList` owner relationship update

```python
# users.py
class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name
```

```python
# tasks.py
import datetime


class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return f"{self.title} (created: {self.date_created}, due: {self.date_due}, completed: {self.completed})"


class RecurringTask(Task):
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime.datetime] = []

    def _compute_next_due_date(self) -> datetime.datetime:
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"
```

```python
# tasklist.py
from tasks import Task


class TaskList:
    def __init__(self, owner: str):
        self.owner = owner
        self.tasks: list[Task] = []

    def get_task(self, ix: int) -> Task:
        return self.tasks[ix]

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        del self.tasks[ix]

    def view_tasks(self) -> None:
        print(f"Task list for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            print(f"{ix}: {task}")
```

```python
# main.py
from tasklist import TaskList
from tasks import Task, RecurringTask
import datetime


def propagate_task_list(task_list: TaskList) -> TaskList:
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))

    r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
    r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)

    task_list.add_task(r_task)
    return task_list


def main() -> None:
    task_list = TaskList("YOUR NAME")
    task_list = propagate_task_list(task_list)
    task_list.view_tasks()


if __name__ == "__main__":
    main()
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Portfolio/exercise_3/src/main.py"
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Quit
Enter your choice: 2
Task list for YOUR NAME:
0: Buy groceries (...)
1: Do laundry (...)
2: Clean room (...)
3: Do homework (...)
4: Walk dog (...)
5: Do dishes (...)
6: Go to the gym - Recurring (...)
```

## Task : Portfolio Exercise 4

Work in `Portfolio/exercise_4/src` using the ToDo app as base.

- Added `users.py` with `User` and `Owner`
- Updated `TaskList` to accept owner as `Owner`
- Updated `main()` to create and pass owner instance

![folder structure](../exercise_4/src/images/image.png)

```python
# users.py
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"User: {self.name}, Email: {self.email}"


class Owner(User):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def __str__(self) -> str:
        return f"Owner: {self.name}, Email: {self.email}"
```

```python
# tasks.py
import datetime


class Task:
    def __init__(self, title: str, date_due: datetime.datetime):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return f"{self.title} | Due: {self.date_due.date()} | Completed: {self.completed}"


class RecurringTask(Task):
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime.datetime] = []

    def _compute_next_due_date(self) -> datetime.datetime:
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        return f"{self.title} (Recurring every {self.interval.days} days) | Next due: {self.date_due.date()}"
```

```python
# tasklist.py
from tasks import Task
from users import Owner


class TaskList:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.tasks: list[Task] = []

    def get_task(self, ix: int) -> Task:
        return self.tasks[ix]

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        del self.tasks[ix]

    def view_tasks(self) -> None:
        print(f"\nTask list for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            print(f"{ix}: {task}")
```

```python
# main.py
from tasklist import TaskList
from tasks import Task, RecurringTask
from users import Owner
import datetime


def propagate_task_list(task_list: TaskList) -> TaskList:
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))

    r_task = RecurringTask("Go to gym", datetime.datetime.now(), datetime.timedelta(days=7))
    task_list.add_task(r_task)

    return task_list


def main() -> None:
    name = input("Enter owner name: ")
    email = input("Enter owner email: ")

    owner = Owner(name, email)
    task_list = TaskList(owner)

    task_list = propagate_task_list(task_list)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Complete a task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "2":
            task_list.view_tasks()
        elif choice == "6":
            break
        # Other choices are implemented in source file.


if __name__ == "__main__":
    main()
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Portfolio/exercise_4/src/main.py"
Enter owner name: Bibek
Enter owner email: raibibek@gmail.com

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Quit
Enter your choice: 2

Task list for Owner: Bibek, Email: raibibek@gmail.com:
0: Buy groceries | Due: 2026-03-14 | Completed: False
1: Do homework | Due: 2026-03-21 | Completed: False
2: Go to gym (Recurring every 7 days) | Next due: 2026-03-18
```
