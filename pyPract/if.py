#!/usr/bin/python3
x = int(input("Enter an integer: "))
if x < 0:
    x = 0
    print("Change negative to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("single")
else:
    print("more")
