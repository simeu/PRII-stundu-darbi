import PySimpleGUI as sg
import sqlite3
import hashlib

conn

# šo grafiskā saskarne neizmanto un varbūt, ka tieši šādā veidā arī nevajag izmantot
# Tie ir kopēšanai derīgi PySG elementi
# Ja vajag vēl vai citādi – veido vai pārveido, ja kaut ko nevajag – izdzēs!
dummylayout = [
    [sg.Text("Klients"), sg.Input(key="-KLIENTA-VARDS-")],
    [sg.Text("Parole"), sg.Input(key="-PAROLE-")],
    [sg.Text("Reģistrācijas datums"), sg.Input(key="-REG-DATUMS-")],
    [sg.Text("e-pasts"), sg.Input(key="-KLIENTA-EPASTS-")],
    [sg.Text("Noskatīto filmu skaits"), sg.Input(key="-KLIENTA-FILMU-SKAITS-")],
    [sg.Text("Filmas nosaukums"), sg.Input(key="-FILMAS-NOSAUKUMS-")],
    [sg.Text("Filmas žanrs"), sg.Input(key="-FILMAS-ZANRS-")],
    [sg.Text("Filmas cena"), sg.Input(key="-FILMAS-EPASTS-")],
    [sg.Text("Seansa datums"), sg.Input(key="-SEANSA-DATUMS-")],
    [sg.Text("Biļešu skaits"), sg.Input(key="-BILESU-SKAITS-")],
    [sg.Button("Saglabāt klientu", key="-SAGLABAT-KLIENTU-")],
    [sg.Button("Saglabāt filmu", key="-SAGLABAT-FILMU-")],
    [sg.Button("Pārdot biļetes", key="-PARDOT-BILETES-")],
    [sg.Button("Parādīt klientu", key="-PARADIT-KLIENTU-")],
    [sg.Button("Parādīt filmu sarakstu", key="-PARADIT-FILMAS-")],
    [sg.Button("Parādīt pardotās biļetes", key="-PARADIT-KASI-")],
]

# Atbilstoši Tevis iecerētajam, kopē PySG elementus šajos layout.
# Ja vajag vairāk par 3, pievieno, ja mazāk – dzēs nost.
layout1 = []
layout2 = []
layout3 = []

# Sakārto ciļņu nosaukumus. Ja sadaļas vairāk par 3, pievieno vēl, ja mazāk, lieko dzēs!
layout = [
    [sg.TabGroup([[sg.Tab("Jauns Seanss", layout1), sg.Tab("Klienta profils", layout2), sg.Tab("Lojalitātes programma", layout3), ]])],
]

window = sg.Window("Kinoteātris", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # izmantoto elementu atslēgas
    """
    "-KLIENTA-VARDS-"
    "-PAROLE-"
    "-REG-DATUMS-"
    "-KLIENTA-EPASTS-"
    "-KLIENTA-FILMU-SKAITS-"
    "-FILMAS-NOSAUKUMS-"
    "-FILMAS-ZANRS-"
    "-FILMAS-EPASTS-"
    "-SEANSA-DATUMS-"
    "-BILESU-SKAITS-"
    """

    if event == "-SAGLABAT-KLIENTU-":
        pass

    if event == "-SAGLABAT-FILMU-":
        pass

    if event == "-PARDOT-BILETES-":
        pass

    if event == "-PARADIT-KLIENTU-":
        pass

    if event == "-PARADIT-FILMAS-":
        pass

    if event == "-PARADIT-KASI-":
        pass

window.close()