import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter do-do",key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box,add_button]],
                   font = ('Helvetica',20))

while True:
    event,values = window.read() #returns a tuple
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos=values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
