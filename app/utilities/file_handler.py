import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)