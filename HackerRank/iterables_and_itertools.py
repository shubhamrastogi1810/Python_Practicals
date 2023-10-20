"""
The input consists of three lines. The first line contains the integer N,
denoting the length of the list. The next line consists of N
space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints
1<= N <= 10
1<= K <= N

All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2

Sample Output

0.8333

Explanation

All possible unordered tuples of length
comprising of indices from 1 to 4 are:
(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
Out of these combinations, of them contain either index or index which are the indices that contain the letter 'a'.
Hence, the answer is 5/6.
"""
from itertools import combinations
le = int(input())
abc = input()
indices = int(input())
abc = ''.join(abc.split(' '))
sets = combinations(abc,indices)
x  =[''.join(i) for i in sets]
cnt = 0
for i in x:
	if 'a' in i:
		cnt+=1
print(round(cnt/len(x),3))
