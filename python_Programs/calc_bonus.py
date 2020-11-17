""" calculate bonus of a  person """
sal = int(input("Enter the salary"))
if sal > 5000:
    bon = sal * 0.05
else:
    bon = sal * 0.03
print("Your bonus is ",bon)
