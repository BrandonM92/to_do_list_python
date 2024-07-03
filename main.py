# IMPORTS
import functions
import time


"""Brandon Mathews - "Python To-Do List" """
"""This is a todo list with various commands that can be used with the name of task on same line. This was me
working with tweaking inputs to allow for single line inputs, stripping the response and having the program operate
differently depending on key words. The main features is to show, create, edit, delete and complete tasks on a to-do list
or planner. All completed tasks are then saved to a new text file for future reference. This can be a useful tool 
when you are doing project managing as the quick and efficient manner to update and adjust will come in handy."""

# Variables
ft = functions
now = time.strftime("%b %d, %Y %H:%M:%S")


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

    todo_list = ft.loadTodoList()  # Load the initial to-do list

    while True:
        user_input = input("\nEnter command or task: ").strip()

        if user_input.lower().startswith("add"):
            task = user_input[len("add"):].strip()
            if task:
                ft.addToList(todo_list, task)
                ft.saveToDoList(todo_list)
            else:
                print("Invalid task format. Please enter a task after 'add'.")

        elif user_input.lower() == "show":
            ft.showTodoList(todo_list, 1)

        elif user_input.lower().startswith("edit"):
            split_input = user_input.split(" | ", maxsplit=1)
            if len(split_input) == 2:
                old_task_name = split_input[0][len("edit "):].strip()
                new_task_name = split_input[1].strip()
                ft.editTask(todo_list, old_task_name, new_task_name)
                ft.saveToDoList(todo_list)
            else:
                print("Invalid edit format. Please use 'edit old_task_name | new_task_name'.")

        elif user_input.lower().startswith("insert"):
            ft.insertNewTask(todo_list)
            ft.saveToDoList(todo_list)

        elif user_input.lower().startswith("complete"):
            task_name = user_input[len("complete"):].strip()
            if task_name:
                ft.completeTask(todo_list, task_name)
                ft.saveToDoList(todo_list)
            else:
                print("Invalid task format. Please enter a task name after 'complete'.")

        elif user_input.lower() == "exit":
            ft.saveToDoList(todo_list)
            break

        elif user_input.lower().startswith("delete"):
            task_name = user_input[len("delete"):].strip()
            if task_name:
                ft.deleteTask(todo_list, task_name)
                ft.saveToDoList(todo_list)
            else:
                print("Invalid task format. Please enter a task name after 'delete'.")

        else:
            print("Invalid option or task format. Please try again.")

    print("End of program")


if __name__ == "__main__":
    main()
