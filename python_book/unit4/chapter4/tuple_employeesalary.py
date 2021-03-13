"""This code will input salaries of no. of employees and will print max. and min. among them."""
number = int(input("Enter the no. of employees you want to enter salary"))
t = tuple()
for i in range(number):
    t+=(int(input()),)

print("Max:-",max(t),"\nMin:-",min(t))
