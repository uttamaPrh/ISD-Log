from tasklist import TaskList
from tasks import Task
import datetime
from typing import Optional


def parse_date(date_value: str) -> Optional[datetime.datetime]:
    """Parse a date string in YYYY-MM-DD format."""
    try:
        return datetime.datetime.strptime(date_value, "%Y-%m-%d")
    except ValueError:
        return None


def parse_index(index_value: str, max_size: int) -> Optional[int]:
    """Parse and validate a task index."""
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

        if choice == "1":
            title = input("Enter a task: ")
            description_input = input("Enter a description (optional): ").strip()
            description = description_input if description_input else None
            input_date = input("Enter a due date (YYYY-MM-DD): ").strip()
            date_object = parse_date(input_date)
            if date_object is None:
                print("Invalid date format. Use YYYY-MM-DD.")
                continue
            task = Task(title, date_object, description)
            task_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            task_list.view_tasks()
        elif choice == "3":
            ix_input = input("Enter the index of the task to remove: ")
            ix = parse_index(ix_input, len(task_list.tasks))
            if ix is None:
                print("Invalid task index.")
                continue
            task_list.remove_task(ix)
            print("Task removed.")
        elif choice == "4":
            ix_input = input("Enter the index of the task to edit: ")
            ix = parse_index(ix_input, len(task_list.tasks))
            if ix is None:
                print("Invalid task index.")
                continue
            print("1. Edit title")
            print("2. Edit due date")
            print("3. Edit description")
            edit_choice = input("Choose an option: ").strip()
            if edit_choice == "1":
                title = input("Enter a new title: ")
                task_list.tasks[ix].change_title(title)
                print("Task title updated.")
            elif edit_choice == "2":
                input_date = input("Enter a new due date (YYYY-MM-DD): ").strip()
                date_object = parse_date(input_date)
                if date_object is None:
                    print("Invalid date format. Use YYYY-MM-DD.")
                    continue
                task_list.tasks[ix].change_date_due(date_object)
                print("Task due date updated.")
            elif edit_choice == "3":
                description_input = input("Enter new description (leave blank to clear): ").strip()
                description = description_input if description_input else None
                task_list.tasks[ix].change_description(description)
                print("Task description updated.")
            else:
                print("Invalid choice.")
        elif choice == "5":
            ix_input = input("Enter the index of the task to complete: ")
            ix = parse_index(ix_input, len(task_list.tasks))
            if ix is None:
                print("Invalid task index.")
                continue
            task_list.tasks[ix].mark_completed()
            print("Task marked as completed.")
        elif choice == "6":
            task_list.view_overdue_tasks()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please choose 1-7.")


if __name__ == "__main__":
    main()
