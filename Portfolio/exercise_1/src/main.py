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
