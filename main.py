"""Brandon Mathews - "Python To-Do List" """
"""This is a todo list with various commands that can be used with the name of task on same line. This was me
working with tweaking inputs to allow for single line inputs, stripping the response and having the program operate
differently depending on key words. The main features is to show, create, edit, delete and complete tasks on a to-do list
or planner. All completed tasks are then saved to a new text file for future reference. This can be a useful tool 
when you are doing project managing as the quick and efficient manner to update and adjust will come in handy."""
# IMPORTS
import time

# VARIABLES
complete_list = []  # List to store completed tasks
filepath = 'todo.txt'
completed_filepath = 'completed_todo.txt'
now = time.strftime("%b %d, %Y %H:%M:%S")

# METHODS
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
        print("Your to-do list is empty.")
    else:
        print("Current To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index + counter}. {task.strip()}")


def addToList(todo_list, task):
    """Adding new tasks to todo list"""
    todo_list.append(task.capitalize() + "\n")


def editTask(todo_list, old_task_name, new_task_name):
    """Edit Tasks and change the name or edit any spelling mistakes"""
    try:
        task_index = todo_list.index(old_task_name.capitalize() + "\n")
        todo_list[task_index] = new_task_name.capitalize() + "\n"
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
        task_index = todo_list.index(task_name.capitalize() + "\n")
        todo_list.pop(task_index)
    except ValueError:
        print("Task not found in the to-do list.")


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


# MAIN GAME LOOP METHOD
def main():
    print("Welcome to the Brandon's To-Do List Manager!")
    print("Commands: 'add task', 'show', 'edit old_task | new_task', 'insert', 'delete task', 'complete task', 'exit'")
    print("Example usage:")
    print("- 'add Go to the store' to add a task.")
    print("- 'edit Go to the store | Buy groceries' to edit a task.")
    print("- 'insert' to insert a task at a specific position.")
    print("- 'delete Buy groceries' to delete a task by name.")
    print("- 'complete Buy groceries' to mark a task as complete.")
    print("- 'exit' to quit the program.")
    print(f"\nDate/Time: {now}")

    todo_list = loadTodoList()  # Load the initial to-do list

    while True:
        user_input = input("\nEnter command or task: ").strip()

        if user_input.lower().startswith("add"):
            task = user_input[len("add"):].strip()
            if task:
                addToList(todo_list, task)
                saveToDoList(todo_list)
            else:
                print("Invalid task format. Please enter a task after 'add'.")

        elif user_input.lower() == "show":
            showTodoList(todo_list, 1)

        elif user_input.lower().startswith("edit"):
            split_input = user_input.split(" | ", maxsplit=1)
            if len(split_input) == 2:
                old_task_name = split_input[0][len("edit "):].strip()
                new_task_name = split_input[1].strip()
                editTask(todo_list, old_task_name, new_task_name)
                saveToDoList(todo_list)
            else:
                print("Invalid edit format. Please use 'edit old_task_name | new_task_name'.")

        elif user_input.lower().startswith("insert"):
            insertNewTask(todo_list)
            saveToDoList(todo_list)

        elif user_input.lower().startswith("complete"):
            task_name = user_input[len("complete"):].strip()
            if task_name:
                completeTask(todo_list, task_name)
                saveToDoList(todo_list)
            else:
                print("Invalid task format. Please enter a task name after 'complete'.")

        elif user_input.lower() == "exit":
            saveToDoList(todo_list)
            break

        elif user_input.lower().startswith("delete"):
            task_name = user_input[len("delete"):].strip()
            if task_name:
                deleteTask(todo_list, task_name)
                saveToDoList(todo_list)
            else:
                print("Invalid task format. Please enter a task name after 'delete'.")

        else:
            print("Invalid option or task format. Please try again.")

    print("End of program")


if __name__ == "__main__":
    main()
