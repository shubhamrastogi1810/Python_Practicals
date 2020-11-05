# calculate gross salary with 40% of DA and HRA is 20%
frmt='{:16}:{:.2f}'
sal = int(input("Enter the salary "))
da = sal*0.4
hra = sal*0.2
gr_sal = sal - da - hra
print("")
print(frmt.format("salary is ",sal))
print(frmt.format("Daily allowance ",da))
print(frmt.format("HRA is ",hra))
print(frmt.format("gross salary is ",gr_sal))
