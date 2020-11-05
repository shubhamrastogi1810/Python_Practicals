# python code to reverse a number
num = int(input("Enter a number "))
f = 0
while num > 0:
	a = num % 10
	f = f*10 + a
	num = num // 10
	
print("reverse of number  is ",f) 
