print("--- DEBUG: FILE IS LOADING ---")

import os

FILENAME = os.path.join(os.path.dirname(__file__), ".." ,"tasks.txt")

def load_tasks():
    """
    Reads tasks from the file and returns them as a list. If the file does not exist, it returns an empty list.
    """
    if not os.path.exists(FILENAME):
        print("No tasks file found. Starting with an empty task list.")
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
      print("Hello from load_tasks!", flush=True)  # Debugging statement
      return [line.strip() for line in file.readlines() if line.strip()]
      

def save_tasks(tasks):
    """
    Save a list of tasks to the text file, overwriting any existing content.
    """
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

if __name__ == "__main__":
   print("Executing test call ...")
   tasks = load_tasks()
   print(f"Loaded tasks: {tasks}")
