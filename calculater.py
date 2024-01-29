#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HomeTown
#
# Created:     13/10/2023
# Copyright:   (c) HomeTown 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------
first=input("entre first number: ")
operater=input("entre operator(+,-,*,/) : ")
second=input("entre second number: ")
first = int(first)
second = int(second)
if operater== "+":
    print(first+second)

elif operater== "-":
    print(first-second)
elif operater== "*":
    print(first*second)

elif operater== "/":
    print(first/second)
else:
    print("invalid number")