"""This program inputs 2 numbers and prints them in ascending order."""
number_1 = int(input("Enter No. 1 "))
number_2 = int(input("Enter No. 2 "))

print("Before Swap.")
print("Number 1",number_1)
print("Number 2",number_2)

number_1 = number_2 + number_1
number_2 = number_2 - number_2
number_1 = number_1 + number_2

print("After Swap.")
print("Number 1",number_1)
print("Number 2",number_2)
