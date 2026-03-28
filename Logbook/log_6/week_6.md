# Session 6 : Debugging, Properties and Persistence

## Section 1 Debugging

### Exercise 1 Task 1 : Finding the Problem

```Python
class Car:

    def __init__(self, initial_speed: int = 0) -> None:
        self.current_speed = initial_speed
        self.distance_km = 0
        self.tick_count = 0

    def accelerate(self) -> None:
        speed_step = 5
        self.current_speed += speed_step

    def brake(self):
        speed_step = 5
        self.current_speed -= speed_step

    def step(self)  -> None:
        self.distance_km += self.current_speed
        self.tick_count += 1

    def average_speed(self) -> float:
        return self.distance_km / self.tick_count


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        menu_choice = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if menu_choice not in "ABOS" or len(menu_choice) != 1:
            print("I don't know how to do that")
            continue
        if menu_choice == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif menu_choice == 'B':
            my_car.brake()
            print("Braking...")
        elif menu_choice == 'O':
            print("The car have drove {} kilometers".format(my_car.distance_km))
        elif menu_choice == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
```

Output
The script was run with one acceleration and two brake inputs, then the odometer value was checked. The distance displayed as 0 km, so behavior was clearly wrong.

For diagnosis, a breakpoint was placed on:

self.distance_km += self.current_speed

Debugger inspection showed the state transition:

After acceleration: current_speed = 5
After braking twice: current_speed = -5

Because speed went below zero, the accumulated distance value was reduced and produced an invalid total.
``` Console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_6/lab_week_6_debugging.py"
I'm a car!
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?A
Accelerating...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?O
The car have drove 0 kilometers
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?S
The car's average speed was -1.25 kph
```

### Exercise 1 Task 2 : Fixing the Problem

``` python
class Car:

    def __init__(self, initial_speed: int = 0) -> None:
        self.current_speed = initial_speed
        self.distance_km = 0
        self.tick_count = 0

    def accelerate(self) -> None:
        speed_step = 5
        self.current_speed += speed_step

    # def brake(self):
    #     self.current_speed -= 5

    def brake(self):
        speed_step = 5
        if self.current_speed >= speed_step:
            self.current_speed -= speed_step
        else:
            self.current_speed = 0

    def step(self)  -> None:
        self.distance_km += self.current_speed
        self.tick_count += 1

    def average_speed(self) -> float:
        return self.distance_km / self.tick_count


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        menu_choice = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if menu_choice not in "ABOS" or len(menu_choice) != 1:
            print("I don't know how to do that")
            continue
        if menu_choice == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif menu_choice == 'B':
            my_car.brake()
            print("Braking...")
        elif menu_choice == 'O':
            print("The car have drove {} kilometers".format(my_car.distance_km))
        elif menu_choice == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
```

``` Console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_6/lab_week_6_debugging.py"
I'm a car!
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?A
Accelerating...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?O
The car have drove 5 kilometers
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?S
The car's average speed was 1.25 kph
```

### Exercise 1 Task 3 : Stepping Through the Code

### Exercise 1 Task 4 : Watching Variables or Expressions 

## Section 2 Properties using the @property decorator
Task: Update `view_tasks` so it displays only pending tasks through the new property.
Use a clear heading like "The following tasks are still to be done:" to indicate filtered output.
Because completed tasks are hidden, preserve original indices by avoiding `enumerate()` on filtered data
and using `index()` when printing each item in the format: `print(f"{ix}: {task}")`.

``` Python
#tasks.py
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
```

``` Python
#tasklist.py
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
```

``` Python
# main.py
import datetime
from tasks import Task, RecurringTask
from tasklist import TaskList


def main():
    owner_name = input("Enter owner name: ")
    todo_app = TaskList(owner_name)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Completed")
        print("5. Exit")

        menu_option = input("Choose: ")

        if menu_option == "1":
            task_title = input("Title: ")
            task_note = input("Description: ")
            deadline_text = input("Due date (YYYY-MM-DD): ")
            deadline = datetime.datetime.strptime(deadline_text, "%Y-%m-%d").date()

            recurring_flag = input("Recurring? (y/n): ")

            if recurring_flag.lower() == "y":
                interval_days = int(input("Interval (days): "))
                repeat_gap = datetime.timedelta(days=interval_days)
                task = RecurringTask(task_title, task_note, deadline, repeat_gap)
            else:
                task = Task(task_title, task_note, deadline)

            todo_app.add_task(task)

        elif menu_option == "2":
            todo_app.view_tasks()

        elif menu_option == "3":
            task_index = int(input("Index: "))
            todo_app.remove_task(task_index)

        elif menu_option == "4":
            task_index = int(input("Index: "))
            selected_task = todo_app.get_task(task_index)
            if selected_task:
                selected_task.mark_completed()
                print("Task updated")

        elif menu_option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
```

Output
``` Console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_6/ToDo/main.py"
Enter owner name: Bibek

1. Add Task      
2. View Tasks    
3. Remove Task   
4. Mark Completed
5. Exit
Choose: 1
Title: Java
Description: Qwerty
Due date (YYYY-MM-DD): 2026-3-30
Recurring? (y/n): 3

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 2
The following tasks are still to be done:
0: Java | Due: 2026-03-30 | ✗

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 4
Index: 0
Task updated

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 2
The following tasks are still to be done:
No remaining tasks

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 5
Goodbye!
```
