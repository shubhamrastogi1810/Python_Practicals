"""This code will input values and will print max and min value among tuple."""
t = tuple()
number = int(input("Enter the no. of values to input"))
for i in range(number):
    t+=(int(input()),)
print("Max:-",max(t),"\nMin:-",min(t))
