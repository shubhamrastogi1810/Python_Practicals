# 1 
# 2 1
# 3 2 1 
# 4 3 2 1
# 5 4 3 2 1
# printing the above pattern

last = int(input("Enter the no. of rows "))
a = 1 

while a<=last:
	b = a
	while b>=1:
		print(b," ",end='')
		b-=1
	print()
	a+=1

