# Nedaudz padomājot, noteikti atcerēsies, kas par uzdevumu bija FizzBuzz
# Ja nu galīgi nē, tad izlasi https://en.wikipedia.org/wiki/Fizz_buzz

# Izpildi FizzBuzz uzdevumu pēc iespējas sarežģītāk

def fizzbuzz():
    for i in range(1, 16):
        if i%5==0 and i%3==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        elif i%5==0 and i%3==0:
            print("FizzBuzz")
        else:
            print(i)