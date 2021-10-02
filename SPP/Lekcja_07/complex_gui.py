import PySimpleGUI as sg


layout = [
    [sg.Text("Some Complex GUI application - just for testing")],
    [sg.Txt("-----------------------------------" * 2)],
    [sg.Button("Some button with No Action")],
    [sg.OK()],
]

window = sg.Window("Main application", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()
