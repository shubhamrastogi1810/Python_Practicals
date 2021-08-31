"""
    This code will compute sum of the digits of the 100!
"""
# Finding the 100 Factorial.
PROD = 1
for i in range(2,101):
    PROD*=i

# Adding the Digits of 100!.
SUM = 0
while PROD > 0:
    TEMP = PROD % 10
    SUM+=TEMP
    PROD //=10
print(SUM)
