from .task_manager import add_task, delete_task, load_into_memory, TASKS

def display_tasks():
    print(f"\n--- TODO APP | {len(TASKS)} Tasks ---")
    if not TASKS:
        print("No tasks available.")
    else:
        for i, task in enumerate(TASKS, start=1):
            print(f"{i}. {task}")

def start():
    load_into_memory()

    while True:
        display_tasks()

        print("\n[1] Add Task")
        print("[2] Delete Task")
        print("[3] Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            task = input("Enter task description: ").strip()
            if task:
                add_task(task)
                print("Task added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            try:
                number = int(input("Enter task number to delete: "))
                removed = delete_task(number - 1)
                if removed:
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")