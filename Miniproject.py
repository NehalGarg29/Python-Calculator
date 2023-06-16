#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nehal
#
# Created:     15-04-2023
# Copyright:   (c) nehal 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num1 = input("Enter first Number : ")
operator = input("Enter operator (+ , - , * , / , %) : ")
num2 = input("Enter second Number : ")
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid Operation")

