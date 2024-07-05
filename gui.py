import FreeSimpleGUI as gui
import functions

# Initial setup


# GUI elements
list_box = gui.Listbox(values=functions.loadTodoList(), key='tasks',
                       enable_events=True, size=(45, 10))

label = gui.Text("Enter a To-do Task")
input_box = gui.InputText(tooltip="Enter To-Do Task", key='todo')
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
delete_button = gui.Button("Delete")
complete_button = gui.Button("Complete")
show_button = gui.Button("Show List")

# Layout of the GUI window
layout = [
    [label],
    [input_box],
    [add_button, edit_button, delete_button, complete_button, show_button],
    [list_box]]

# Create the window
window = gui.Window("My To-Do App", layout=layout, font=('Arial', 20))


def update_todo_listbox():
    update_todo = functions.loadTodoList()
    window['tasks'].update(values=update_todo)


# Event loop for the GUI
while True:
    event, values = window.read()
    # print(event)
    # print(values)
    # print(values['tasks'])

    if event == gui.WIN_CLOSED:
        break
    elif event == "Add":
        new_todo = values['todo']
        print(new_todo)
        if new_todo.strip():
            todos = functions.loadTodoList()
            functions.addToList(todos, new_todo)
            functions.saveToDoList(todos)
            update_todo_listbox()
    elif event == "Edit":
        todo_to_edit = values['tasks'][0]
        new_todo = values['todo']

        todos = functions.loadTodoList()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.saveToDoList(todos)
        update_todo_listbox()
    elif event == "Delete":
        selected_task = values['tasks'][0]  # Assuming single selection
        todos = functions.loadTodoList()
        if selected_task:
            todo_list = functions.deleteTask(todos,selected_task)
            functions.saveToDoList(todo_list)
            update_todo_listbox()
    elif event == "Complete":
        pass  # Implement complete functionality if needed
    elif event == "Insert":
        pass  # Implement insert functionality if needed
    elif event == "Show List":
        todos = functions.loadTodoList()
        show_todo_list = functions.showTodoList(todos, 1)
        gui.popup(show_todo_list)

# Close the window when the loop ends
window.close()
