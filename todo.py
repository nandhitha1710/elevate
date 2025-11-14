# Simple To-Do List (Beginner Friendly)

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Menu actions
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def remove_task():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except:
        print("Invalid number!")

# Main loop
while True:
    print("\n--- To-Do Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Choose: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
