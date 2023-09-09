num = int(input())

for i in range(0,num):
	try:
		a,b = map(int,input().split(' '))
		print(a//b)
	except ZeroDivisionError as e:
		print("Error Code: ",e)
	except ValueError as v:
		print("Error Code: ",v)

	
