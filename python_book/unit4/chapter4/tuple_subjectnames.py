"""This code will input names of subjects and will print it."""
value = int(input("Enter the no. of subjects"))
t = tuple()
for i in range(value):
    t+=(input(),)

print(t)
