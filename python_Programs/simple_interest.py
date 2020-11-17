"""  calculate simple interset """
FRMT = '{:10}:{:.2f}'
amount = int(input("Enter the principal amount"))
rate = float(input("Enter the Rate"))
years = int(input("Enter the Years"))
SI = (amount * rate * years)/ 100
print(FRMT.format("Simple interest",SI))
