#swap 2 numbers in python
frmt='{:10}:{:}'
a = int(input("Enter num. 1 "))
b = int(input("Enter num. 2 "))
print("Before swapping ") 
print(frmt.format("Num 1",a))
print(frmt.format("Num 2",b))

a = b - a
b = b - a
a = a + b

print("After swapping ")
print(frmt.format("Num 1",a))
print(frmt.format("Num 2",b))
