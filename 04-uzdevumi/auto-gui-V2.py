import PySimpleGUI as sg
from autoV2 import Auto

razotaji =["Audi", "BMW", "Chrysler", "Dacia"]
# krasas = ["Balta", "Sarkana", "Melna"]

layout = [
    [sg.Text("Ražotājs", size=12), sg.Combo(values=razotaji, key="-RAZOTAJI-")],
    # [sg.Text("Ražotājs", size=12), sg.Input(key="-RAZOTAJI-")],
    [sg.Text("Modelis", size=12), sg.Input(key = "-MODELIS-")],
    [sg.Text("Gads", size=12), sg.Input(key = "-GADS-")],
    [sg.Text("Cena", size=12), sg.Input(key = "-CENA-")],
    [sg.Text("Nobraukums", size=12), sg.Input(key = "-NOBRAUKUMS-")],
    # [sg.Text("Krāsa"), sg.Combo(values=krasas, key="-KRASA-")],
    [sg.CalendarButton("Iegādes datums", target = "-DATUMS-", format="%Y-%m-%d", locale="lv_LV", begin_at_sunday_plus=1), sg.Input(key = "-DATUMS-")],
    # [sg.Text("Iegādes datums", size=12), sg.Input(key = "-DATUMS-")],
    [sg.Button("Saglabāt", size=12), sg.Button("Palielināt nobraukumu", size=23, key="-PALIELINAT-"), sg.Button("Iziet", size=12)],
    [sg.Text(key = "-APRAKSTS-")]
]

window = sg.Window("Auto", layout)

while True:
    event, values = window.read()
    # print(event, values)

    if event == "Iziet" or event == sg.WINDOW_CLOSED:
        break

    if event == "Saglabāt":
        marka = values["-RAZOTAJI-"]
        modelis = values["-MODELIS-"]
        gads = int(values["-GADS-"])
        cena = int(values["-CENA-"])
        nobraukums = int(values["-NOBRAUKUMS-"])
        # krasa = values("-KRASA-")
        datums = values["-DATUMS-"]

        masina = Auto(marka, modelis, cena, gads, datums, nobraukums)
        teksts = masina.paradit()
        window["-APRAKSTS-"].update(teksts)

    if event == "-PALIELINAT-":
        nobraukuma_izmainas = int(sg.popup_get_text("Par cik palielināt?"))

        masina.palielinat_nobraukumu(nobraukuma_izmainas)
        masina.paradit()

window.close()