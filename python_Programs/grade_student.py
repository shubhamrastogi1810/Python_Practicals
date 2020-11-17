""" assign a grade to a student by his marks of 5 subjects """
LIS = []
for i in range(0,5):
    print("Enter sub",i+1,"marks")
    A = int(input())
    LIS.append(A)
print()
TOTOAL = 0
for i in LIS:
    TOTAL+=int(i)
PER = TOTAL / len(LIS)
A =0
for i in LIS:
    if i <= 40:
        A = 1
if A == 0:
    if PER >= 60:
        print("You got First division with per ",PER)
    elif 50<= PER < 60:
        print("You got Second Division with per ",PER)
    elif 40 <= PER < 50:
        print("You got Third Division with per ",PER)
else:
    print("You are Fail.")
