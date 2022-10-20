import PySimpleGUI as sg
import gramatas as gr
import json

sg.theme("Black")


menu = [
    ["Fails", ["Saglabāt kā JSON"]],
    ["Palīdzība", ["Par programmu"]]
]

layout1 = [
    [sg.Text("Labrīt/Labdien/Labvakar! \nŠī ir grāmatu aplikācija, kas ļauj jums sekot līdzi jūsu ienākumiem, grāmatu skaitam, u. tml.")],
    [sg.Text("Lūdzu, ievadat grāmatas nosaukumu."), sg.Input(key = "-B-")],
    [sg.Text("Lūdzu, ievadat grāmatas autoru."), sg.Input(key = "-A-")],
    [sg.Text("Lūdzu, ievadat nopirko grāmatu skaitu."), sg.Input(key = "-S-")],
    [sg.Text("Lūdzu, ievadat grāmatas cenu."), sg.Input(key = "-C-")],
    [sg.Button("Ievadīt"), sg.Text(key = "-X-")],
    [sg.Button("Iziet"), sg.Text(key = "-Y-")],
]

layout2 = [[sg.Button("Saglabāt kā JSON", size = 18)]]

layout3 = [[sg.Button("Apraksts", size = 12)]]

layout_main = [
    [sg.Menu(menu)],
    [sg.TabGroup([[sg.Tab("Ievade", layout1)], [sg.Tab("Saglabāt", layout2)], [sg.Tab("Apraksts", layout3)]])]
]

win = sg.Window("Grāmatu reģistrēšana", layout_main)
while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Ievadīt":
        nosaukums = values["-B-"]
        autors = values["-A-"]
        skaits = values["-S-"]
        cena = values["-C-"]
        gramatas = gr.Gramata(nosaukums, autors, skaits, cena)
        gramatas.paradit()
        print("Grāmata reģistrēta!")

    if event == "Iziet":
        win.close()

    if event == "Saglabāt kā JSON":
        gramatas.veido_vardnicu()
        gramatas.saglabat() # Pie šīs rindas met ārā error'u "TypeError: saglabat() takes 0 positional arguments but 1 was given".
        gramatas.paradit()

    if event == "Apraksts":
        sg.popup("Šī ir programma, kuru veidoja 18 gadīga meitene, pusnaktī, negulējusi, pirms programmēšanas kontroldarba.")
