import FreeSimpleGUI as gui
import functions

information = (
    "Welcome to Brandon's To-Do List Manager!\n"
    "Commands: 'add task', 'show', 'edit old_task | new_task', 'insert', 'delete task', 'complete task', 'exit'\n"
    "Example usage:\n"
    "- 'add Go to the store' to add a task.\n"
    "- 'edit Go to the store | Buy groceries' to edit a task.\n"
    "- 'insert' to insert a task at a specific position.\n"
    "- 'delete Buy groceries' to delete a task by name.\n"
    "- 'complete Buy groceries' to mark a task as complete.\n"
    "- 'exit' to quit the program.\n"
)


label = gui.Text("Enter a Command (To-do Task)")
input_box = gui.InputText(tooltip="Enter To-Do Task")
button = gui.Button("Submit")
info_label = gui.Text(information)
window = gui.Window("My To-Do App", layout=[[label,input_box,button],[info_label]])
window.read()
window.close()
