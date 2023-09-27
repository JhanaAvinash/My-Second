class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

tasks = []

def add_task():
    task_description = input("Enter the task description: ")
    task = Task(task_description)
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    task_index = int(input("Enter the task index to update: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index!")
        return
    new_task_description = input("Enter the new task description: ")
    tasks[task_index].description = new_task_description
    print("Task updated successfully!")

def mark_task_completed():
    task_index = int(input("Enter the task index to mark as completed: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index!")
        return
    tasks[task_index].completed = True
    print("Task marked as completed!")

def show_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("Tasks:")
    for i, task in enumerate(tasks):
        status = "Completed" if task.completed else "Not Completed"
        print(f"{i}. {task.description} - {status}")

while True:
    print("\n--- To-Do List Application ---")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Mark Task as Completed")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        show_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")