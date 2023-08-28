numbers = []
n= int(input("Enter value for n "))
for i in range(2,n+1):
    for j in range(2,n+1):
        if i ** j not in numbers:
            numbers.append(i**j)
print(len(numbers))
