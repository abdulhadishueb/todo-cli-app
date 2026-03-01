import os
import json

FILENAME = os.path.join(os.path.dirname(__file__), ".." ,"tasks.json")


def load_tasks():
    # If file does not exist, return empty list
    if not os.path.exists(FILENAME):
        print("No tasks file found. Starting with an empty task list.")
        return {"tasks": [],"users": []}
    try:
      with open(FILENAME, "r", encoding="utf-8") as file:
        print("Hello from load_tasks!", flush=True)  # Debugging statement
        data = json.load(file)

        if isinstance(data, list):
            return {"tasks": data,"users": []}

        return data

        
    except json.JSONDecodeError:
        return {"tasks": [],"users": []}
      

def save_tasks(data):
    """
    Save a list of tasks to the text file, overwriting any existing content.
    """
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
           
if __name__ == "__main__":
   print("Executing test call ...")
   data = load_tasks()
   print(f"Loaded database: {data}")
