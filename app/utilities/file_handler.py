import os

# tasks.txt will be created in the project root
FILENAME = "tasks.txt"


def load_tasks():
    # If file does not exist, return empty list
    if not os.path.exists(FILENAME):
        return []

    tasks = []

    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:   # ignore empty lines
                tasks.append(line)

    return tasks


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")