import PySimpleGUI as sg
import tehnikas_noma as te
import json
from datetime import datetime

sg.theme("Black")

menu = [
    ["Faili", ["Saglabāt kā JSON"]],
    ["Palīdzība", ["Par programmu"]]
]

layout1 = [ 
    [sg.Text("Labrīt/Labdien/Labvakar! \nŠī ir tehnikas nomas aplikācija, kas ļauj Jums sekot līdzi jūsu ienākumiem, nomāto preču skaitam, u. tml.")],
    [sg.Text("Lūdzu, ievadat tehnikas veidu, piem., zāģis, urbis."), sg.Input(key = "-B-")],
    [sg.Text("Lūdzu, ievadat tehnikas nosaukumu."), sg.Input(key = "-A-")],
    [sg.Text("Lūdzu, ievadat īsu aprīkojuma aprakstu."), sg.Input(key = "-S-")],
    [sg.Text("Lūdzu, ievadat grāmatas cenu dienā."), sg.Input(key = "-C-")],
    [sg.Text("Lūdzu, ievadat aprīkojuma pieejamību."), sg.Input(key = "-P-")],
    [sg.Text("Lūdzu, ievadat nomnieka vārdu."), sg.Input(key = "-D-" )],
    [sg.Text("Lūdzu, ievadat nomnieka uzvārdu."), sg.Input(key = "-E-")],
    [sg.Text("Lūdzu, ievadat nomnieka personas kodu."), sg.Input(key = "-F-")],
    [sg.Text("Lūdzu, ievadat nomnieka telefona numuru."), sg.Input(key = "-G-")],
    [sg.CalendarButton("Nomas sākuma datums", target = "-DATUMS-", format="%Y-%m-%d", locale="lv_LV", begin_at_sunday_plus=1), sg.Input(key = "-DATUMS-")],
    [sg.CalendarButton("Nomas beigu datums", target = "-DATUMS2-", format="%Y-%m-%d", locale="lv_LV", begin_at_sunday_plus=1), sg.Input(key = "-DATUMS2-")],
    [sg.Button("Ievadīt"), sg.Text(key = "-X-")],
    [sg.Button("Iziet"), sg.Text(key = "-Y-")],

]

layout2 = [[sg.Button("Saglabāt kā JSON", size = 20)]]

layout3 = [[sg.Button("Apraksts", size = 20)]]

layout4 = [[sg.Button("Rādīt", size = 20)]]

layout_main = [ 
    [sg.Menu(menu)],
    [sg.TabGroup([[sg.Tab("Ievade", layout1)], [sg.Tab("Saglabāt", layout2)], [sg.Tab("Apraksts", layout3)], [sg.Tab("Rādīt", layout4)]])]
]

win = sg.Window("Tehnikas nomas reģistrācija", layout_main)
while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Ievadīt":
        kategorija = values["-B-"]
        nosaukums = values["-A-"]
        raksturojums = values["-S-"]
        cena = values["-C-"]
        pieejamiba = values["-P-"]
        vards = values["-D-"]
        uzvards = values["-E-"]
        pkods = values["-F-"]
        tel = values["-G-"]
        sakdat = values["-DATUMS-"]
        beigdat = values["-DATUMS2-"]

        tehnika = te.Noma(kategorija, nosaukums, raksturojums, cena, pieejamiba, vards, uzvards, pkods, tel, sakdat, beigdat)
        tehnika.paradit()
        sg.popup("Noma reģistrēta!")

    if event == "Iziet":
        win.close()

    if event == "Saglabāt kā JSON":
        tehnika.vardnica()
        tehnika.saglaba()
        tehnika.paradit()

    if event == "Apraksts":
        sg.popup("Programma, kur skaitļi un tehnika kopā ballē.")

    if event == "Par programmu":
        sg.popup("Programma, kur skaitļi un tehnika kopā ballē.")
    
    if event == "Rādīt":
        tehnika.aprekini()
