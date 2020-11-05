# assign a grade to a student by his marks of 5 subjects
lis = []
for i in range(0,5):
	print("Enter sub",i+1,"marks")
	a = int(input())	
	lis.append(a)
print()	
total = 0
for i in lis:
	total+=int(i)
per = total / len(lis)
a =0
for i in lis:
	if i <= 40:
		a = 1
if a == 0:
	if per >= 60:
		print("You got First division with per ",per)
	elif per >= 50 and per < 60:
		print("You got Second Division with per ",per)
	elif per >= 40 and per < 50:
                print("You got Third Division with per ",per)
else:
	print("You are Fail.")
	

