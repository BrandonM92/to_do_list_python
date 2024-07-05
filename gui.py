import FreeSimpleGUI as gui
import functions


# Function to update the list box with current to-do items
def update_todo_listbox(main_window):
    """
    Updates the list box in the GUI window with the current to-do items.

    Args:
    - window (gui.Window): The GUI window object.

    Returns:
    - None
    """
    update_todo = functions.loadTodoList()
    indexed_todos = [(index_count, task.strip()) for index_count, task in enumerate(update_todo)]
    main_window['tasks'].update(values=indexed_todos)


# GUI elements
list_box = gui.Listbox(values=[], key='tasks', enable_events=True, size=(45, 10))

label = gui.Text("Enter a To-do Task")
input_box = gui.InputText(tooltip="Enter To-Do Task", key='todo')
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
delete_button = gui.Button("Delete")
complete_button = gui.Button("Complete")
insert_button = gui.Button("Insert")
show_button = gui.Button("Show List")

# Layout of the GUI window
layout = [
    [label],
    [input_box],
    [add_button, edit_button, delete_button, complete_button, insert_button, show_button],
    [list_box]
]

# Create the window
window = gui.Window("My To-Do App", layout=layout, font=('Arial', 20))

# First read to initialize the window and handle events
event, values = window.read()

# Initial update of the to-do list box after the window is shown
update_todo_listbox(window)

# Event loop for the GUI
while True:
    if event == gui.WIN_CLOSED:
        break
    elif event == "Add":
        new_todo = values['todo']
        if new_todo.strip():
            todos = functions.loadTodoList()
            functions.addToList(todos, new_todo)
            functions.saveToDoList(todos)
            update_todo_listbox(window)
            window['todo'].update('')  # Clear input box after adding task

    elif event == "Edit":
        selected_task = values['tasks']
        if selected_task:
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.loadTodoList()
                index = selected_task[0][0]  # Get index from selected task
                old_task = selected_task[0][1]
                functions.editTask(todos, old_task, new_todo)
                functions.saveToDoList(todos)
                update_todo_listbox(window)
                window['todo'].update('')  # Clear input box after editing task

    elif event == "Delete":
        selected_task = values['tasks']
        if selected_task:
            todos = functions.loadTodoList()
            index = selected_task[0][0]  # Get index from selected task
            todo_list = functions.deleteTask(todos, todos[index])
            functions.saveToDoList(todo_list)
            update_todo_listbox(window)

    elif event == "Complete":
        selected_task = values['tasks']
        if selected_task:
            todos = functions.loadTodoList()
            index = selected_task[0][0]  # Get index from selected task
            functions.completeTask(todos, todos[index])
            functions.saveToDoList(todos)
            update_todo_listbox(window)

    elif event == "Insert":
        selected_task = values['tasks']
        new_todo = values['todo']
        if selected_task:
            todos = functions.loadTodoList()
            index = selected_task[0][0]  # Get index from selected task
            functions.insertNewTask(todos, new_todo, index)
            functions.saveToDoList(todos)
            update_todo_listbox(window)
            window['todo'].update('')  # Clear input box after inserting task

    elif event == "Show List":
        todos = functions.loadTodoList()
        show_todo_list = functions.showTodoList(todos, 1)
        gui.popup(show_todo_list)

    # Read the next event
    event, values = window.read()

# Close the window when the loop ends
window.close()
