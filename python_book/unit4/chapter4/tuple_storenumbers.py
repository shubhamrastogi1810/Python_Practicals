"""This code will input tuple values and will print it."""
number = int(input("Enter the number to input"))
print("Enter the numbers")
t = tuple()
for i in range(number):
    t +=(int(input()),)
print(t)
