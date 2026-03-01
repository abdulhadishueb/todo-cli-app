from .task_manager import add_task, delete_task, load_into_memory, TASKS
from rich import print
def display_tasks():
    load_into_memory()
    print(f"[green bold]\nTODO APP | \n{len(TASKS)} Tasks[/green bold]")
    if not TASKS:
        print("No tasks available.")
    else:
        for i, task in enumerate(TASKS, start=1):
            print(f"{i}. {task}")

def start():
    

    while True:
        
        display_tasks()

        print("\n1. Add Task.")
        print("2. Delete Task.")
        print("3. Exit.")

        choice = input("Select an option: ").strip()

        if choice == "1":
            task = input("Type your task to be stored: ").strip()
            if task:
                add_task(task)
                print("Task added successfully.")
            else:
                print("Enter any task.")

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
            print("[yellow bold]\nAdd Tasks so you dont forget[/yellow bold]")
            break

        else:
            print("Invalid option. Please try again.")