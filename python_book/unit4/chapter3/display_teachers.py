"""This program will input n numbers of record with name and number of teachers."""
FRMT = '{:4} : {:}'
teachers = {}
filevar = open("teacher_read.txt","r")
total_teachers = int(input("Enter the total number of teachers."))
for i in range(total_teachers):
    number,name = filevar.readline().split(',')
    teachers[number] = name
filevar.close()
print("\n\t Teachers Info.\n")
for i in teachers:
    print(FRMT.format(i,teachers[i]))
