from .file_handler import load_tasks, save_tasks

def main():
    # Example usage
    tasks = load_tasks()
    print("Current tasks:", tasks)
    
    # Add a new task
    new_task = "Buy coffee"
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added and saved.")

if __name__ == "__main__":
    main()