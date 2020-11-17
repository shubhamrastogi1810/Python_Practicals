""" This program is used to perform basic arithmatic operations """
FRMT = '{:17} :{:.2f}'
a = float(input("Enter Num1. "))
b = float(input("Enter Num2. "))
print(FRMT.format("Addition is",a+b))
print(FRMT.format("Subtraction is",a-b))
print(FRMT.format("Multiplication is",a*b))
print(FRMT.format("Division is",a/b))
