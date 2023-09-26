import PySimpleGUI as ps

ltodo = ps.Text('Type a ToDo')
btodo = ps.InputText(tooltip='Enter a ToDo')
badd_todo = ps.Button('Add')

window = ps.Window('ToDo App', layout=[[ltodo], [btodo, badd_todo]])
window.read()
window.close()
