# to find a factorial of a number 
no = int(input("Enter a number "))
f = 1
while (no > 1):
	f*=no 
	no-=1
print("factorial no is ",f)
