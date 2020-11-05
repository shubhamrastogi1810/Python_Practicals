# calculate simple interset
frmt = '{:10}:{:.2f}'
amount = int(input("Enter the principal amount"))
rate = float(input("Enter the Rate"))
years = int(input("Enter the Years"))
si = (amount * rate * years)/ 100
print(frmt.format("Simple interest",si))
