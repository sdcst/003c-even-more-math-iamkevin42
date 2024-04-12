#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""
import math

a = int(input("Enter a length in centimeters so I can convert it into feet and inches\n"))

feet = int(a // 30.48)
inches = float((a - feet * 30.48) / 2.54)


print(f"{a} cm is {feet} feet and {inches} inches")