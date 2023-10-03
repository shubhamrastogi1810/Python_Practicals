"""
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11

cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2

Task

You are given two arrays A and B. Both have dimensions of N X N.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N.
The next lines contains space separated integers of array A.
The following lines contains space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.

Sample Input

2
1 2
3 4
1 2
3 4

Sample Output

[[ 7 10]
 [15 22]]

"""
import numpy as np
a = []
b = []
n = int(input())
for i in range(n):
	val = list(map(int,input().strip().split()))
	a.append(val)
a = np.array(a)
for i in range(n):
	val = list(map(int,input().strip().split()))
	b.append(val)
b = np.array(b)
print(a@b)
