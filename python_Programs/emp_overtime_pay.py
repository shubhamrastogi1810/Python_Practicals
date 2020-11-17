""" pay overtime to the employee if work > 40 hrs """

worktime = float(input("Enter the work time of employee "))
if worktime >= 40:
    pay = (worktime - 40)*12
    print("overtime pay is ",pay)
else:
    print("no overtime")
