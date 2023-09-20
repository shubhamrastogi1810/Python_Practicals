"""
Input Format

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

Constraints
1 <= N,M <= 1000
0 <= K < M
Each Element <= 1000

Output Format

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation 0

The details are sorted based on the second attribute, since K is zero-indexed. 

"""


nm = input().split(' ')
row = int(nm[0])
column = int(nm[1])
array = []
for i in range(row):
	array.append(list(map(int, input().rstrip().split(' '))))
k = int(input())
array.sort(key = lambda array : array[k])
for i in range(row):
	for j in range(column):
		print(array[i][j],end=' ')
	print()

