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