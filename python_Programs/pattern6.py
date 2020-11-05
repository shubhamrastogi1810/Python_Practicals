# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2 
# 1
# printing the above pattern

last = int(input("Enter the no. of rows "))
a = last 

while a>=1:
	b = 1
	while b<=a:
		print(a," ",end='')
		b+=1
	print()
	a-=1

