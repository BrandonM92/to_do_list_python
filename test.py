import FreeSimpleGUI as gui


feet_text = gui.Text("Enter Feet")
input_1 = gui.InputText()
input_2 = gui.InputText()
inch_text = gui.Text("Enter Inches")
convert_button = gui.Button("Convert")
window = gui.Window("Converter", layout=[[feet_text,input_1],[inch_text,input_2],[convert_button]])
window.read()
window.close()
