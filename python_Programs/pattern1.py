# * 
# * *
# * * * 
# * * * *
# * * * * *
# printing the above pattern

last = int(input("Enter the no. of rows "))
a = 1 

while a<=last:
	b = 1
	while b<=a:
		print(" *",end='')
		b+=1
	print()
	a+=1

