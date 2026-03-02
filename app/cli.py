from rich import print
from . import task_manager as tm
import json

FILENAME = "tasks.json"

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
class TodoCLI:

    def display_tasks(self):
        

        print(f"[bold green]\nTODO APP | \n There are {len(tm.TASKS)} Tasks currently[/bold green]")

        if not tm.TASKS:
            print("[red]No tasks available.[/red]")
        else:
            for i, task in enumerate(tm.TASKS, start=1):
                status = "[green]✔ Completed[/green]" if task["completed"] else "[yellow]• Pending[/yellow]"
                print(f"[cyan]{i}.[/cyan] {task['description']}- {status}")

    def add_task_ui(self):
        task = input("Type your task to be stored: ").strip()

        if task:
            tm.add_task(task)
            print("[green]Task added successfully.[/green]")
        else:
            print("[red]Enter any task.[/red]")

    def delete_task_ui(self):
        try:
            number = int(input("Enter task number to delete: "))
            removed = tm.delete_task(number - 1)

            if removed:
                print(f"[green]Removed:[/green] {removed}")
            else:
                print("[red]Invalid task number.[/red]")

        except ValueError:
            print("[red]Please enter a valid number.[/red]")
    def completed(self):
        try:
            number = int(input("Enter task number to mark as completed: "))

            success = tm.complete_task(number - 1)

            if success:
                    print("[green]Task marked as completed.[/green]")
            else:
                    print("[red]Invalid task number.[/red]")

        except ValueError:
                print("[red]Please enter a valid number.[/red]")
    def start(self):
        tm.load_into_memory()
        while True:

            self.display_tasks()
            print("\n1. View all your tasks.")
            print("2. Add Task.")
            print("3. Delete Task.")
            print ("4. Completed")
            print("5. Exit.")

            choice = input("Select an option: ").strip()
            

            if  choice == "1":
                
            elif choice == "1":
                self.add_task_ui()

            elif choice == "2":
                self.delete_task_ui()
            elif choice == "3":
                self.completed()

            elif choice == "4":
                print("[bold yellow]Come back![/bold yellow]")
                break

            else:
                print("[red]Invalid option. Please try again.[/red]")


def start():
    cli = TodoCLI()
    cli.start()