import ctypes
import sys

# EXERCISE 1

firstVar = "Python 2023"
secondVar = "Python 2023"
thirdVar = "Python 2023"

print(f"Content equality: {firstVar == secondVar == thirdVar}")

print(f"firstVar {type(firstVar)} {hex(id(firstVar))}")
print(f"secondVar {type(secondVar)} {hex(id(secondVar))}")
print(f"thirdVar {type(thirdVar)} {hex(id(thirdVar))}")

thirdVar = "Java 11"

print("\n After reassigning variable d")
print(f"Content equality: {firstVar == secondVar == thirdVar}")
print(f"thirdVar {type(thirdVar)} {hex(id(thirdVar))}")

# EXERCISE 2

firstOperand = int(input("Insert first number: "))
secondOperand = int(input("Insert second number: "))
operator = input("Insert operator: ")

if operator == "+":
    print(f"{firstOperand} + {secondOperand} = {firstOperand + secondOperand}")
elif operator == "-":
    print(f"{firstOperand} - {secondOperand} = {firstOperand - secondOperand}")
elif operator == "*":
    print(f"{firstOperand} * {secondOperand} = {firstOperand * secondOperand}")
elif operator == "/":
    print(f"{firstOperand} / {secondOperand} = {firstOperand / secondOperand}")

# EXERCISE 3

questionsDictionary = {

    "1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:": [
        "1. oglądanie telewizji/filmów/seriali",
        "2. czytanie książek/czasopism",
        "3. słuchanie muzyki",
        "4. spotkania z rodziną/przyjaciółmi",
    ],

    "2. W jakich okolicznościach czytasz książki najczęściej?": [
        "1. podczas podróży",
        "2. w czasie wolnym (po pracy, na urlopie)",
        "3. podczas pracy/nauki (to ich element)",
        "4. w ogóle nie czytam",
    ],

    "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?:": [
        "1. chęć poszerzenia wiedzy",
        "2. czytanie mnie relaksuje/odpręża",
        "3. fakt, że czytanie jest modne",
        "4. czytanie to moje hobby",
    ],

    "4. Po książki w jakiej formie sięgasz najczęściej?": [
        "1. papierowej (tradycyjnej)",
        "2. e-booki (książki elektroniczne) na komputerze",
        "3. e-booki na tablecie/telefonie",
        "4. e-booki na specjalnym czytniku (np. Kindle)",
    ],

    "5. Ile książek czytasz średnio w ciągu roku?": [
        "1. żadnej w całości - jedynie fragmenty",
        "2. 2 lub 3",
        "3. 4-10",
        "4. powyżej 10",
    ],

    "6. Jak często średnio czytasz książki?": [
        "1. codziennie",
        "2. raz w tygodniu",
        "3. raz w miesiącu",
        "4. raz na kilka miesięcy",
    ],

    "7. Po jakie gatunki książek sięgasz najczęściej?": [
        "1. kryminały/thrillery",
        "2. fantastykę",
        "3. psychologiczne",
        "4. podróżnicze",
    ],

}


