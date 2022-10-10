import PySimpleGUI as sg

#sg.theme_previewer()

izkartojums = [
[sg.Text("Username"), sg.Input(key = "-USER-")],
[sg.Text("Password"), sg.Input(key = "-PASS-")],
[sg.Button("OK"), sg.Text(key = "-X-")]
]

logs = sg.Window("Log-in", izkartojums)

while True:
    notikums, vertibas = logs.read()
    print(notikums, vertibas)
    if notikums == sg.WINDOW_CLOSED:
        break
    if notikums == "OK":
        vards = vertibas["-USER-"]
        uzvards = vertibas["-PASS-"]
        vardsuzvards = f"{vards}, {uzvards}"
        logs["-X-"].update(vardsuzvards)

logs.close()