import time

# VARIABLES
complete_list = []  # List to store completed tasks
filepath = 'to-do.txt'
completed_filepath = 'completed_todo.txt'
now = time.strftime("%b %d, %Y %H:%M:%S")


def saveToDoList(todo_list):
    """
    Saves the current to-do list to 'to-do.txt'.

    Args:
    - todo_list (list): The list of tasks to be saved.

    Returns:
    - None
    """
    try:
        with open(filepath, 'w') as file:
            file.writelines(todo_list)
    except IOError as e:
        print(f"An error occurred while saving the to-do list: {e}")


def showTodoList(todo_list, counter):
    """
    Generates a formatted string representation of the to-do list.

    Args:
    - todo_list (list): The list of tasks to display.
    - counter (int): Starting number for indexing tasks.

    Returns:
    - str: Formatted string representation of the to-do list.
    """
    if not todo_list:
        return "Your to-do list is empty."
    else:
        result = "Current To-Do List: \n"
        for index, task in enumerate(todo_list):
            result += f"{index + counter}. {task.strip()} \n"
        return result


def addToList(todo_list, task):
    """
    Adds a new task to the to-do list.

    Args:
    - todo_list (list): The list of tasks to add the new task to.
    - task (str): The task to add.

    Returns:
    - None
    """
    todo_list.append(task + "\n")


def editTask(todo_list, old_task_name, new_task_name):
    """
    Edits a task in the to-do list.

    Args:
    - todo_list (list): The list of tasks to edit.
    - old_task_name (str): The name of the task to be replaced.
    - new_task_name (str): The new name for the task.

    Returns:
    - None
    """
    try:
        task_index = todo_list.index(old_task_name + "\n")
        todo_list[task_index] = new_task_name + "\n"
        print(f"Task '{old_task_name}' updated to '{new_task_name}'.")
    except ValueError:
        print("Task not found in the to-do list.")


def insertNewTask(todo_list, new_task, index):
    """
    Inserts a new task at a specific index in the to-do list.

    Args:
    - todo_list (list): The list of tasks to insert the new task into.
    - new_task (str): The task to insert.
    - index (int): The index where the new task should be inserted.

    Returns:
    - None
    """
    try:
        # Validate the index
        if 0 <= index <= len(todo_list):
            # Add \n to new_task if it doesn't already have it
            if not new_task.endswith("\n"):
                new_task += "\n"

            # Insert new_task at the specified index
            todo_list.insert(index, new_task)
            print(f"Task '{new_task.strip()}' inserted at index {index} successfully.")
        else:
            print(f"Index {index} is out of range. Appending '{new_task.strip()}' at the end.")

    except ValueError:
        print("Error occurred while inserting the task.")


def deleteTask(todo_list, task_name):
    """
    Deletes a task from the to-do list.

    Args:
    - todo_list (list): The list of tasks to delete the task from.
    - task_name (str): The name of the task to delete.

    Returns:
    - list or str: Updated todo_list after deletion, or error message if task not found.
    """
    try:
        task_index = todo_list.index(task_name)
        todo_list.pop(task_index)
        return todo_list
    except ValueError:
        return "Task not found in the to-do list."


def completeTask(todo_list, task_name):
    """
    Completes a task and moves it to 'completed_todo.txt'.

    Args:
    - todo_list (list): The list of tasks containing the task to complete.
    - task_name (str): The name of the task to complete.

    Returns:
    - list: Updated todo_list after completing the task.
    """
    try:
        task_index = todo_list.index(task_name)
        completed_task = todo_list.pop(task_index).strip()

        try:
            with open(completed_filepath, 'a') as file:
                if file.tell() != 0:
                    file.write("\n" + completed_task)  # Write task on new line if file isn't empty
                else:
                    file.write(completed_task)  # Write task without leading newline for first entry
            print(f"'{completed_task}' has been completed and moved to 'completed_todo.txt'")
        except IOError as e:
            print(f"An error occurred while saving the completed task: {e}")

    except ValueError:
        print("Task not found in the to-do list.")

    return todo_list  # Return the updated todo_list after completing the task


def loadTodoList():
    """
    Loads the to-do list from 'to-do.txt'.

    Returns:
    - list: The loaded list of tasks from 'to-do.txt'.
    """
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []
    except IOError as e:
        print(f"An error occurred while loading the to-do list: {e}")
        return []
