from rich import print
from .utilities.file_handler import load_tasks, save_tasks, FILENAME

TASKS = []

def load_into_memory():
    TASKS.clear()
    loaded = load_tasks()

    for item in loaded:
        if isinstance(item, str):
            TASKS.append({
                "description": item,
                "completed": False
            })
        else:
            TASKS.append(item)

def add_task(task):
    TASKS.append({
        "description": task,
        "completed": False
    })
    save_tasks(TASKS)
    print(f"DEBUG: [blue bold]Saved {len(TASKS)} tasks to[/blue bold] {FILENAME}")

def complete_task(index):
    if 0 <= index < len(TASKS):
        TASKS[index]["completed"] = True
        save_tasks(TASKS)
        return True
    return False

def delete_task(index):
    if 0 <= index < len(TASKS):
        removed = TASKS.pop(index)
        save_tasks(TASKS)
        return removed
    return None