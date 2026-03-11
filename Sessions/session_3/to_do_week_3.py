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

