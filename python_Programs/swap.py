""" swap 2 numbers in python """
FRMT='{:10}:{:}'
a = int(input("Enter num. 1 "))
b = int(input("Enter num. 2 "))
print("Before swapping ")
print(FRMT.format("Num 1",a))
print(FRMT.format("Num 2",b))

a = b - a
b = b - a
a = a + b

print("After swapping ")
print(FRMT.format("Num 1",a))
print(FRMT.format("Num 2",b))
