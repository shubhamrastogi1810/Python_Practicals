"""
The code computes the difference of sum of square and square of the sum of first 100 natural numbers
"""

# sum of the squares of first 100 natural numbers.
SUMSQ = 0
for i in range(1,101):
    SUMSQ+=i**2


# square of the sum of first 100 natural numbers.
SUMS = 0
for i in range(1,101):
    SUMS += i
SUMS = SUMS**2
print(SUMS - SUMSQ)
