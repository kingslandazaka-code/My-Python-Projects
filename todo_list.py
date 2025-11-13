# === Simple To-Do List ===

def add_task(task_list):
    task = input("Enter a task to add: ")
    task_list.append(task)
    print("Task added.")

def view_tasks(task_list):
    print("=== Your Tasks ===")
    if len(task_list) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(task_list)):
            print(i+1, "-", task_list[i])

def remove_task(task_list):
    view_tasks(task_list)
    if len(task_list) > 0:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(task_list):
            removed = task_list.pop(index)
            print("Removed task:", removed)
        else:
            print("Invalid number.")

def todo_list_app():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice!")

todo_list_app()
