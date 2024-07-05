---

# To-Do Task Manager

## Overview
This To-Do Task Manager is a simple Python application designed to help users manage their 
tasks efficiently. It provides a graphical user interface (GUI) for adding, editing, 
deleting, completing tasks, and displaying the current to-do list. 

## Features
- **Add Task**: Allows users to add new tasks to the to-do list.
- **Edit Task**: Enables users to edit existing tasks by replacing them with new ones.
- **Delete Task**: Lets users remove tasks from the to-do list.
- **Complete Task**: Marks tasks as completed and moves them to a separate completed tasks file.
- **Insert Task**: Inserts a new task at a specific position in the to-do list.
- **Show List**: Displays the current to-do list in a pop-up window.

## Usage
1. **Starting the Program**: Run `main.py` to launch the ToDo List Manager.
2. **Commands**:
   - **Add**: Type `add <task>` to add a new task.
   - **Edit**: Type `edit <old_task> | <new_task>` to edit an existing task.
   - **Delete**: Type `delete <task>` to remove a task from the list.
   - **Complete**: Type `complete <task>` to mark a task as completed.
   - **Insert**: Type `insert` to insert a task at a specific position.
   - **Show List**: Type `show` to display the current to-do list.
   - **Exit**: Type `exit` to quit the program.
3. **GUI**: The program includes a GUI with buttons and input fields for easy task management.
4. **File Storage**: Tasks are stored in `todo.txt` and completed tasks are saved in `completed_todo.txt`.
5. **Error Handling**: The program handles common errors gracefully, such as task not found or file I/O errors.

## Requirements
- Python 3 (Created on 3.10.7)
- FreeSimpleGUI (included)
- Standard Python libraries

## Notes
- Make sure `todo.txt` and `completed_todo.txt` are in the same directory as `main.py`.
- If you want to organize the `txt` files into their own folder, update the path directory.
- Ensure Python and necessary libraries are installed and up-to-date.

## Author
- **Author**: Brandon Mathews
- **Contact**: [bjmathews@hotmail.com](mailto:bjmathews@hotmail.com)

---

