# Session 3 : Python Functions, Scope and Errors

- [Session 3 : Python Functions, Scope and Errors](#session-3--python-functions-scope-and-errors)
  - [Section 1 Functions and Scope](#section-1-functions-and-scope)
    - [Exercise 1 Task 1 : Functions in Python](#exercise-1-task-1--functions-in-python)
    - [Exercise 2 Task 2 : Variable Scope](#exercise-2-task-2--variable-scope)
  - [Section 2 Assertions and Errors](#section-2-assertions-and-errors)
    - [Exercise 1 Task 1 : Assertions](#exercise-1-task-1--assertions)
    - [Exercise 1 Task 2 : Identifying and Fixing Common Errors](#exercise-1-task-2--identifying-and-fixing-common-errors)
  - [Section 3 Your first larger-scale Python programme](#section-3-your-first-larger-scale-python-programme)

## Section 1 Functions and Scope

### Exercise 1 Task 1 : Functions in Python

```python
# Greeting Message
participant_list = ["Uttam", "Aarav", "Sita"]


def greet(person_name):
    print(f"Hello {person_name}")


for person in participant_list:
    greet(person)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_3/lab_week_3.py"
Hello Uttam
Hello Aarav
Hello Sita
```

```python
# Task 2: Tax calculation

def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax


calculated_tax = calculate_tax(72000, 0.22)
print("Calculated Tax:", calculated_tax, "pounds")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_3/lab_week_3.py"
Calculated Tax: 15840.0 pounds
```

```python
# Task 3: Compound interest calculator

def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    for year in range(1, duration + 1):
        total_for_year = principal * (1 + interest_rate) ** year
        print(f"Year {year}: {total_for_year:.2f} pounds")

    final_amount = principal * (1 + interest_rate) ** duration
    return int(final_amount)


result = compound_interest(1500, 4, 0.06)
print("Final amount:", result)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_3/lab_week_3.py"
Year 1: 1590.00 pounds
Year 2: 1685.40 pounds
Year 3: 1786.52 pounds
Year 4: 1893.72 pounds
Final amount: 1893
```

### Exercise 2 Task 2 : Variable Scope

```python
# Exercise 2 Task 2: Variable Scope

counter = 0


def increment_local():
    counter = 5
    print("Inside function, counter =", counter)


increment_local()
print("Outside function, counter =", counter)
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_3/lab_week_3.py"
Inside function, counter = 5
Outside function, counter = 0
```

## Section 2 Assertions and Errors

### Exercise 1 Task 1 : Assertions

```python
# Exercise 1 Task 1: Assertions

assert len("ISD") == 3, "Length check should pass."
assert 10 < 5, "This assertion is intentionally false."
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_3/lab_week_3.py"
Traceback (most recent call last):
  File "d:\assignments\t2\ISD\ISD log\Sessions\session_3\lab_week_3.py", line 54, in <module>
    assert 10 < 5, "This assertion is intentionally false."
AssertionError: This assertion is intentionally false.
```

### Exercise 1 Task 2 : Identifying and Fixing Common Errors

```python
# Exercise 1 Task 2: Identifying and Fixing Common Errors

# Syntax error example
print("Hello, Python!")

# Name error example
message = "Ready to run"
print(message)

# Value/type conversion example
number_text = "12"
number_value = 8
result_sum = int(number_text) + number_value
print("The sum is:", result_sum)

# Index error example
sample_list = [1, 2, 3]
# print(sample_list[5])


def fixed_indent_function():
    print("Indentation is correct.")
```

## Section 3 Your first larger-scale Python programme

```python
# In this exercise, you will create a simple to-do list program using Python. You will use variables, lists, input,
# loops, functions, and conditionals to build a basic but functional to-do list manager.
# Task: To-Do list manager
# You need to create a to-do list manager with the following functionalities:
# 1. Initialize an empty list to store tasks.
# 2. Implement a menu that allows the user to perform the following actions:
# • Add a new task to the list.
# • View the current tasks in the list.
# • Remove a task from the list.
# • Quit and exit the program.
# 3. Use a while loop to repeatedly display the menu and handle user input.
# 4. Create functions for adding, viewing, and removing tasks.
# 5. Use conditionals to execute the appropriate function based on the user's choice.
# 6. Display a message if the user tries to remove a task that doesn't exist.
# 7. Exit the program when the user chooses to quit.

tasks = []


def add_task():
    task_name = input("Enter task title: ")
    tasks.append(task_name)
    print("Task saved.")


def view_tasks():
    if len(tasks) == 0:
        print("Task list is currently empty.")
    else:
        print("Current task list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def remove_task():
    if len(tasks) == 0:
        print("Nothing to remove.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid integer.")


while True:
    print("\nStudy To-Do Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Program closed.")
        break
    else:
        print("Invalid choice. Select 1, 2, 3, or 4.")
```

Output

```console
PS D:\assignments\t2\ISD\ISD log> & C:\Users\ujjwa\AppData\Local\Python\pythoncore-3.14-64\python.exe "d:/assignments/t2/ISD/ISD log/Sessions/session_3/to_do_week_3.py"

Study To-Do Manager
1. Add task
2. View tasks
3. Remove task
4. Exit
Choose option (1-4): 1
Enter task title: Python revision
Task saved.

Study To-Do Manager
1. Add task
2. View tasks
3. Remove task
4. Exit
Choose option (1-4): 1
Enter task title: Database notes
Task saved.

Study To-Do Manager
1. Add task
2. View tasks
3. Remove task
4. Exit
Choose option (1-4): 2
Current task list:
1. Python revision
2. Database notes

Study To-Do Manager
1. Add task
2. View tasks
3. Remove task
4. Exit
Choose option (1-4): 3
Current task list:
1. Python revision
2. Database notes
Enter task number to delete: 2
Removed: Database notes

Study To-Do Manager
1. Add task
2. View tasks
3. Remove task
4. Exit
Choose option (1-4): 4
Program closed.
```
