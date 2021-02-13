"""This program takes length and initial angle as input, and calculates horizontal displacement."""
# horizontal displacement equation
# X(T) = L × cos(A × cos(T × √9.8/L)) - L × cos(A)

import math
L = float(input())
A = float(input())
for i in range(0,10):
    x = L * math.cos(A * math.cos(i *(9.8/L)**0.5)) - (L * math.cos(A))
    print(x)
