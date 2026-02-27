
from  utilities.file_handler import load_tasks, save_tasks, FILENAME

TASKS = []

def load_into_memory():
    global TASKS
    TASKS = load_tasks()

def add_task(task):
    TASKS.append(task)
    save_tasks(TASKS)  # Sync to disk
    print(f"---DEBUG: Saved {len(TASKS)} tasks to {FILENAME}---")

def delete_task(index):
    if 0 <= index < len(TASKS):
        removed = TASKS.pop(index)
        save_tasks(TASKS)  # Sync to disk
        return removed
    return None

if __name__ == "__main__":
    load_into_memory()
    
    while True:
        print(f"\n--- TODO APP | {len(TASKS)} Tasks ---")
        for i, task in enumerate(TASKS, start=1):
            print(f"{i}. {task}")
        
        print("\n[1] Add  [2] Delete  [3] Exit")
        choice = input("Selection: ")

        if choice == "1":
            val = input("Task description: ")
            if val.strip():
               add_task(val)
            else:
               print("Task cannot be empty.")
        elif choice == "2":
            try:
                user_num = int(input("Task number to remove: "))
                target_index = user_num - 1
                removed_task = delete_task(target_index)
                
                if removed_task:
                    print(f"Successfully removed: {removed_task}")
                else:
                    print(f"Invalid selection: Task #{user_num} does not exist.")
                    
            except (ValueError, IndexError):
                print("Invalid selection.")
        elif choice == "3":
            print("Goodbye!")
            break