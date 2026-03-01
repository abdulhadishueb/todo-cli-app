from rich import print
from .task_manager import add_task, delete_task, load_into_memory, TASKS

class TodoCLI:

    def display_tasks(self):
        

        print(f"[bold green]\nTODO APP | \n{len(TASKS)} Tasks[/bold green]")

        if not TASKS:
            print("No tasks available.")
        else:
            for i, task in enumerate(TASKS, start=1):
                print(f"[cyan]{i}.[/cyan] {task}")

    def add_task_ui(self):
        task = input("Type your task to be stored: ").strip()

        if task:
            add_task(task)
            print("[green]Task added successfully.[/green]")
        else:
            print("[red]Enter any task.[/red]")

    def delete_task_ui(self):
        try:
            number = int(input("Enter task number to delete: "))
            removed = delete_task(number - 1)

            if removed:
                print(f"[green]Removed:[/green] {removed}")
            else:
                print("[red]Invalid task number.[/red]")

        except ValueError:
            print("[red]Please enter a valid number.[/red]")

    def start(self):
        load_into_memory()
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