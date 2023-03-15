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
