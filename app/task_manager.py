from rich import print
from  .utilities.file_handler import load_tasks, save_tasks, FILENAME

TASKS = []

def load_into_memory():
    TASKS.clear()
    TASKS.extend(load_tasks())

def add_task(task):
    TASKS.append(task)
    save_tasks(TASKS)  # Sync to disk
    print(f"DEBUG:[blue bold] Saved {len(TASKS)} tasks to[/blue bold] {FILENAME}")

def delete_task(index):
    if 0 <= index < len(TASKS):
        removed = TASKS.pop(index)
        save_tasks(TASKS)  # Sync to disk
        return removed
    return None

