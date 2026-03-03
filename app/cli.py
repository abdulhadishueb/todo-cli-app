from rich import print
from . import task_manager as tm

class TodoCLI:
    
    def display_tasks(self):
        

        print(f"[bold green]\nTODO APP: \n There are/is {len(tm.TASKS)} Tasks currently[/bold green]")

        if not tm.TASKS:
            print("[red]No tasks available.[/red]")
        else:
            for i, task in enumerate(tm.TASKS, start=1):
                status = "[green] Completed ✔[/green]" if task["completed"] else "[red]- Pending...[/red]"
                print(f"[cyan]{i}.[/cyan] {task['description']}- {status}")

    def add_task_ui(self):
        task = input("Type your task to be stored: ").strip()

        if task:
            tm.add_task(task)
            print("[green]Task added successfully.[/green]")
        else:
            print("[red]Enter any task.[/red]")

    def delete_task(self):
        self.display_tasks()
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
            done = int(input("Enter task number to mark as completed: "))

            success = tm.complete_task(done - 1)

            if success:
                    print("[green]Task marked as completed.[/green]")
            else:
                    print("[red]Invalid task number.[/red]")

        except ValueError:
                print("[red]Please enter a valid number.[/red]")
    def start(self):
        tm.load_into_memory()
        while True:
            print("\n1. View all your tasks.")
            print("2. Add Task.")
            print("3. Delete Task.")
            print ("4. Completed")
            print("5. Exit.")

            choice = input("Select an option: ").strip()
            

            if  choice == "1":
                self.display_tasks()
                
            elif choice == "2":
                self.add_task_ui()

            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.completed()

            elif choice == "5":
                print("[bold yellow]Come back![/bold yellow]")
                break

            else:
                print("[red]Invalid option. Please try again.[/red]")


def start():
    cli = TodoCLI()
    cli.start()