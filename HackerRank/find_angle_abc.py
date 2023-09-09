import math
ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 + bc**2)

degree = math.acos(bc/ac)

print(str(round(math.degrees(degree)))+u"\u00b0")

