# ✅ Todo CLI App

A modular Python Command-Line Interface (CLI) To-Do application built as a group project.

It lets you manage tasks from the terminal, and it **saves tasks to a JSON file** so they still exist after you close and re-run the program.

---

## 🚀 Features

- View all tasks
- Add a new task
- Delete a task
- Mark a task as completed ✅
- Persistent storage using **JSON** (`app/tasks.json`)
- Clean terminal output using the **rich** library
- Modular structure (separation of CLI, logic, and storage)

---

## 🧠 How Persistence Works (Important)

Tasks are stored in:

- `app/tasks.json`

When the app starts, it loads tasks from `tasks.json` into memory.
When you add/delete/complete a task, it updates the list and saves back to `tasks.json`.

> If you still have `tasks.txt` in the repo, it’s legacy/old storage.  
> Your current code is using **JSON**, so `tasks.txt` is not needed (unless your team still uses it somewhere).

---

## 📦 Requirements

- Python 3.x
- rich

Install dependency:

```bash
pip install rich
▶️ How to Run

From the project root folder:

python __main__.py
📂 Project Structure
todo-cli-app/
├── __main__.py
├── README.md
├── .gitignore
├── tasks.txt                
└── app/
    ├── __init__.py
    ├── cli.py
    ├── task_manager.py
    ├── tasks.json
    └── utilities/
        ├── file_handler.py
        
👥 Team Members

Abdulhadi Mohamed — File Persistence

Amon-Sudo — CLI Development

Brian Wairagi — Task Logic 

🧩 Concepts Demonstrated

Modular Python project structure

Separation of concerns (UI vs logic vs storage)

File I/O (JSON read/write)

Basic error handling (invalid input)

Object-Oriented Programming (OOP) using TodoCLI class

Git feature-branch workflow collaboration

✅ Demo Flow

Run the app

Add tasks

View tasks

Mark a task as completed

Delete a task

Restart the app and confirm tasks still exist (loaded from tasks.json)