""" This program inputs employee's name and number and sorts them according to thier numbers."""
# write a program to input 'n' employee number and name and to display all
# employee's information in ascending order besed upon their number.
FRMT = "{:6}  :  {:}"
employee_info = {}
total_employee = int(input("Enter the total number of employees. "))
filevar = open("employee_read.txt","r")
for i in range(total_employee):
    number,name = filevar.readline().split(',')
    employee_info[int(number)] = name
filevar.close()
print("\n Employee  Information\n ")
for i in sorted(employee_info.keys()):
    print(FRMT.format(i,employee_info.get(i)))
