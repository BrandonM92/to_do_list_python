import time

""" This file contains all my methods used in the main.py file"""

# VARIABLES
complete_list = []  # List to store completed tasks
filepath = 'todo.txt'
completed_filepath = 'completed_todo.txt'
now = time.strftime("%b %d, %Y %H:%M:%S")


def saveToDoList(todo_list):
    """Saves To Do List"""
    # Save the current to-do list to 'todo.txt'
    try:
        with open(filepath, 'w') as file:
            file.writelines(todo_list)
    except IOError as e:
        print(f"An error occurred while saving the to-do list: {e}")


def showTodoList(todo_list, counter):
    """Displays To Do List"""
    if not todo_list:
        return "Your to-do list is empty."
    else:
        result = "Current To-Do List: \n"
        for index, task in enumerate(todo_list):
            result += f"{index + counter}. {task.strip()} \n"
        return result


def addToList(todo_list, task):
    """Adding new tasks to todo list"""
    todo_list.append(task + "\n")


def editTask(todo_list, old_task_name, new_task_name):
    """Edit Tasks and change the name or edit any spelling mistakes"""
    try:
        task_index = todo_list.index(old_task_name + "\n")
        todo_list[task_index] = new_task_name+ "\n"
        print(f"Task '{old_task_name}' updated to '{new_task_name}'.")
    except ValueError:
        print("Task not found in the to-do list.")


def insertNewTask(todo_list):
    """If you are worried about ordering lists in order of importance, we have the functionality to edit or
    change the order of the items individually"""
    try:
        showTodoList(todo_list, 0)
        new_task = input("Enter new task name: ").capitalize().strip() + "\n"

        print(
            f"Choose where to insert '{new_task.strip()}'. Enter the index number (0 to {len(todo_list)}) or leave "
            f"empty to append at the end.")
        position_input = input("Index to insert (leave empty for end): ").strip()

        if position_input.isdigit():
            position = int(position_input)
            if 0 <= position < len(todo_list):
                todo_list.insert(position, new_task)
            else:
                print(f"Index {position} is out of range. Inserting at the end of the list.")
                todo_list.append(new_task)
        elif position_input == "":
            todo_list.append(new_task)
        else:
            print("Invalid input. Inserting at the end of the list.")
            todo_list.append(new_task)

        print(f"Task '{new_task.strip()}' inserted successfully.")
    except ValueError:
        print("Invalid input. Inserting at the end of the list.")
        new_task = ""  # Assign an empty string in case of ValueError
        todo_list.append(new_task)


def deleteTask(todo_list, task_name):
    """Allows user to delete tasks from list"""
    try:
        task_index = todo_list.index(task_name)
        todo_list.pop(task_index)
        return todo_list
    except ValueError:
        return "Task not found in the to-do list."


def completeTask(todo_list, task_name):
    """This method handles completing tasks and saving them to new txt file while also removing them from todo.txt"""
    try:
        task_index = todo_list.index(task_name.capitalize() + "\n")
        completed_task = todo_list.pop(task_index).strip()
        complete_list.append(completed_task)

        # Append the completed task to the 'completed_todo.txt' file
        try:
            with open(completed_filepath, 'a') as file:
                file.write(completed_task + "\n")
                print(f"'{completed_task}' has been completed, moved to the completed_todo.txt")
        except IOError as e:
            print(f"An error occurred while saving the completed task: {e}")

    except ValueError:
        print("Task not found in the to-do list.")


def loadTodoList():
    """Loads the to-do list (todo.txt)"""
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []
    except IOError as e:
        print(f"An error occurred while loading the to-do list: {e}")
        return []
