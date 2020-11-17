""" calculate gross salary with 40% of DA and HRA is 20% """
FRMT='{:16}:{:.2f}'
salary= int(input("Enter the salary "))
da= salary*0.4
hra = salary*0.2
gr_sal = salary - da - hra
print("")
print(FRMT.format("salary is ",salary))
print(FRMT.format("Daily allowance ",da))
print(FRMT.format("HRA is ",hra))
print(FRMT.format("gross salary is ",gr_sal))
