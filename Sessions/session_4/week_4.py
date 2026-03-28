import datetime


class Task:
    def __init__(self, title, date_due):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due

    def change_title(self, new_title):
        self.title = new_title

    def change_due_date(self, new_due_date):
        self.date_due = new_due_date

    def display(self):
        print("Title:", self.title)
        print("Created:", self.date_created)
        print("Due Date:", self.date_due)


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, date_due):
        task = Task(title, date_due)
        self.tasks.append(task)

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks):
                print("\nTask", index + 1)
                task.display()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted.")
        else:
            print("Invalid task number.")

    def edit_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            print("\n1. Change Title")
            print("2. Change Due Date")
            choice = input("Choose option: ")
            if choice == "1":
                new_title = input("Enter new title: ")
                task.change_title(new_title)
            elif choice == "2":
                new_due_date = input("Enter new due date: ")
                task.change_due_date(new_due_date)
            else:
                print("Invalid choice.")
        else:
            print("Invalid task number.")


def main():
    task_list = TaskList()

    while True:
        print("\n----- Task Manager -----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date: ")
            task_list.add_task(title, due_date)
        elif choice == "2":
            task_list.view_tasks()
        elif choice == "3":
            task_list.view_tasks()
            num = int(input("Enter task number to edit: ")) - 1
            task_list.edit_task(num)
        elif choice == "4":
            task_list.view_tasks()
            num = int(input("Enter task number to delete: ")) - 1
            task_list.delete_task(num)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
