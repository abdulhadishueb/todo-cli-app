📝 Todo CLI App
📌 Project Overview

This is a modular Python Command-Line Interface (CLI) To-Do application developed as a group project.

The application allows users to:

Add tasks

View tasks

Delete tasks

The system uses file-based persistence, meaning tasks are saved to a local file (tasks.txt) and remain available even after the program is closed and restarted.

👥 Team Members

Abdulhadi Mohamed – Project Lead 

Amon-Sudo – CLI Development

Brian Wairagi – Task Logic & File Persistence

🚀 Features

Interactive CLI menu

Add new tasks

View existing tasks

Delete tasks

Persistent storage using tasks.txt

Modular folder structure

Git feature-branch workflow

🗂️ Project Structure
todo-cli-app/
├── main.py
├── tasks.txt
├── README.md
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── task_manager.py
│   └── utilities/
│       ├── __init__.py
│       └── file_handler.py
▶️ How to Run the Application

1️⃣ Clone the repository:

git clone <repository-url>

2️⃣ Navigate into the project directory:

cd todo-cli-app

3️⃣ Install required dependency:

pip install rich

4️⃣ Run the application:

python main.py
💾 Data Persistence

Tasks are saved inside a file called:

tasks.txt

This file is automatically created when the first task is added.

When the application starts, tasks are loaded from this file into memory.

🔄 Git Collaboration Workflow

We followed a feature-branch workflow:

Each team member worked on a separate feature branch

Meaningful commit messages were used

Pull Requests were created for each feature

Changes were reviewed before merging into the main branch

This ensured clean collaboration and structured version control.

📚 Concepts Demonstrated

Modular Python project structure

Separation of concerns

File Input/Output (File I/O)

Basic error handling

Object-Oriented Programming (OOP)

Feature-branch Git workflow

Team collaboration

✅ Demo Flow

The application demonstrates:

Adding a task

Viewing tasks

Deleting tasks

Restarting the application and confirming tasks persist