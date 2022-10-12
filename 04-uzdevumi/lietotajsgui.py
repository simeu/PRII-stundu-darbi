import PySimpleGUI as sg
import lietotajs as li

sg.theme("Black")

izkartojums = [
[sg.Text("Laipni lūgts mūsu nezināmajā portālā!")],
[sg.Text("Ievadiet savu lietotājvārdu"), sg.Input(key = "-USER-")],
[sg.Text("Ievadiet savu paroli"), sg.Input(key = "-PASS-")],
[sg.Button("OK"), sg.Text(key = "-X-")]
]

izk = [
[sg.Text("Ierakstīšanās pabeigta!")],
[sg.Button("OK"), sg.Text(key = "-Y-")]
]

logs = sg.Window("Nezināmās programmas ierakstīšanās", izkartojums)

while True:
    notikums, vertibas = logs.read()
    if notikums == sg.WINDOW_CLOSED:
        break
    if notikums == "OK":
        print("Ierakstīšanās veiksmīga!")
        logs.close()