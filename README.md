# Todo CLI App

## 📌 Project Overview

This is a modular Python Command-Line Interface (CLI) To-Do application developed as a group project.

The application allows users to:
- Add tasks
- View tasks
- Delete tasks

The system uses file-based persistence, meaning tasks are saved to a local file and remain available even after the program is closed and restarted.

This project demonstrates:
- Modular Python structure
- Separation of concerns
- File I/O persistence
- Git collaboration using feature branches and Pull Requests

---

## 👥 Team Members

- **Abdulhadi Mohamed** – Project Lead & Integration
- **Amon-Sudo** – CLI Development
- **BrianWairagi** – Task Logic & File Persistence

---

## 🚀 Features

- Interactive CLI menu
- Add new tasks
- View existing tasks
- Delete tasks
- Persistent storage using `tasks.txt`
- Modular folder structure
- Git feature-branch workflow

---

## 🗂️ Project Structure


todo-cli-app/
├── main.py
├──.gitignore
├── README.md
├── app/
│ ├── init.py
│ ├── cli.py
│ ├── task_manager.py
│ └── utilities/
│ ├── init.py
│ └── file_handler.py



## ▶️ How to Run the Application

1. Clone the repository:

git clone <repository-url>


2. Navigate to the project directory:

cd todo-cli-app


3. Run the application:

python main.py


---

## 💾 Data Persistence

The application saves tasks to a local file named:


tasks.txt


This ensures that tasks remain saved even after restarting the program.

---

## 🔄 Git Collaboration Workflow

We followed a feature-branch workflow:

- Each team member worked on a separate feature branch
- Changes were committed with meaningful messages
- Pull Requests were created for each feature
- Features were merged into the `main` branch after review

This allowed clean collaboration and structured version control.

---

## 📚 Concepts Demonstrated

- Modular Python project structure
- Separation of concerns
- File Input/Output (File I/O)
- Basic error handling
- Feature-branch Git workflow
- Team collaboration

---

## ✅ Demo Flow

The application can demonstrate:

1. Adding a task
2. Viewing tasks
3. Exiting the application
4. Restarting and confirming tasks persist

---