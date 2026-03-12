# Portfolio Log

## Week 4 Portfolio Entry

This week focused on classes, objects, modularizing code, and portfolio extensions to the To-Do application.
Based on the Week 4 practical brief, the portfolio work was split into two exercises.

### Exercise 1

This exercise contains the first portfolio extension.
It builds on the modularized To-Do application and adds an optional description field to each task.

```text
exercise_1/
	src/
		main.py
		tasklist.py
		tasks.py
```

Summary:
- `tasks.py` adds an optional `description` attribute to the `Task` class.
- `tasks.py` also adds a `change_description` method.
- `main.py` allows the user to add and edit task descriptions.
- `tasklist.py` manages the list of task objects.

### Exercise 2

This exercise contains the second portfolio extension.
It adds overdue-task viewing to the task manager.

```text
exercise_2/
	src/
		__pycache__/
			tasklist.cpython-314.pyc
			tasks.cpython-314.pyc
		main.py
		tasklist.py
		tasks.py
```

Summary:
- `tasklist.py` includes a `view_overdue_tasks` method.
- `main.py` adds an additional menu option so the user can display overdue tasks.
- `tasks.py` keeps the task data model used by the application.
- `__pycache__` was generated after importing the modules in Python.

### Notes

- The Week 4 portfolio implementation was based on the tasks described in `Practical Week 4 - 25_26.pdf`.
- Exercise 1 implements the optional task description extension.
- Exercise 2 implements the overdue-task viewing extension.
