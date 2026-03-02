from rich import print
from . import task_manager as tm
class TodoCLI:

    def display_tasks(self):
        

        print(f"[bold green]\nTODO APP | \n There are {len(tm.TASKS)} Tasks currently[/bold green]")

        if not tm.TASKS:
            print("[red]No tasks available.[/red]")
        else:
            for i, task in enumerate(tm.TASKS, start=1):
                print(f"[cyan]{i}.[/cyan] {task}")

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

    def start(self):
        tm.load_into_memory()
        while True:

            self.display_tasks()

            print("\n1. Add Task.")
            print("2. Delete Task.")
            print("3. Exit.")

            choice = input("Select an option: ").strip()

            if choice == "1":
                self.add_task_ui()

            elif choice == "2":
                self.delete_task_ui()

            elif choice == "3":
                print("[bold yellow]Come back![/bold yellow]")
                break

            else:
                print("[red]Invalid option. Please try again.[/red]")


def start():
    cli = TodoCLI()
    cli.start()