import math
import json
import os
# Nedaudz padomājot, noteikti atcerēsies, kas par uzdevumu bija FizzBuzz
# Ja nu galīgi nē, tad izlasi https://en.wikipedia.org/wiki/Fizz_buzz
# Izpildi FizzBuzz uzdevumu pēc iespējas sarežģītāk
#def fizzbuzz():
 #   for i in range(1, 16):
  #      if i%5==0 and i%3==0:
   #         print("FizzBuzz")
    #    elif i%3==0:
     #       print("Fizz")
     #   elif i%5==0:
     #         print("Buzz")
     #   elif i%5==0 and i%3==0:
     #       print("FizzBuzz")
     #  else:
     #      print(i)


def fizzbuzz():
    print("Sveicināts(-a)! Šis būs ārkārtīgi sarežģītais testa veida uzdevums, kurš tev jaatrisina.\nJa tu to nespēsi atrisināt, tad tu esi dārzenis. :)")
    v = input(print("Vai matemātiku zini? J/N"))
    d = input(print("Vai zini, kas ir dalīšana? J/N"))
    if d == "J" or "j":
        print("Malacis. Dosimies tālāk")
        fizzbuzz2()

def fizzbuzz2():
    print("Esmu pārliecinājies, ka pamata zināšanas tev ir.\nDosimies tālāķ.")
    if not os.path.exists("fizzbuzz.json"):
        cipari = ""
        dati = json.dumps(cipari)
        with open ("fizzbuzz.json", "w", encoding = "utf-8") as fails:
            fails.write(dati)
    else:
        with open("fizzbuzz.json", "r", encoding = "utf-8")as fails:
            dati = fails.read()
            print(dati)

    c = input(print("Uzspēlēsim spēli, kuru sauc FizzBuzz. Noteikumi ir vienkāŗši.\nIr doti vārdi 'Fizz' un 'Buzz'. Es sākšu skaitīt no viens, un mēs uz maiņām teiksim skaitļus.\nĀķis ir tāds: Ja skaitlis/cipars dalās ar 3, tad skaitļa vietā ir jāsaka 'fizz',\nbet, ja skaitlis dalās ar 5, tad ir jāsaka buzz.\nJa skaitlis dalās gan ar 3, gan ar 5, tad jāsaka 'fizzbuzz.'\nSaprati? J/N"))
    if c == "J" or "j":
        print("Malacis! Tad varam sākt!")
        fizzbuzz3()
    else:
        print("Pārlasi vēlreiz.")

def fizzbuzz3():
    print("Labi!! Tad es sākšu. Skaitīsim līdz 100. 1...")
    nr = ""
    if nr%3==0 or "Fizz":
        print("Fizz! Pareizi")
    elif nr%5==0 or "Buzz":
        print("Buzz!")
    else:
        print("Tev nu gan matemātika švaka... sāksim no sākuma.")

fizzbuzz3()


def saglabashana():
    with open("fizzbuzz.json", "w", encoding = "utf-8")as fails:
            dati = fails.write()
            print(dati)


# Vēlējos uztaisīt tā, ka programma automātiski atbild uz cilvēka ievadīto, bet, lai nebūtu visu laiku jāraksta "if ...:". Tā kā vēlos, lai
# spēle strādātu līdz skaitlim 100, tad ir jāizmanto for cikls, bet nezinu, kā to varētu ievadīt kodā, lai būtu korekti.
# Sapratu domu noformatēšanai, ka var taisīt 1  1, 2 2, 3 fizz, utt., tomēr nezinu, kā to pareizi noformatēt. 
# Kods neiet korekti. Nesaprotu, kādēļ.


