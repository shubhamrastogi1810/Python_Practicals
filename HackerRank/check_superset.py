set_val = set(map(int,input().split(' ')))
num = int(input())
lis = []
val = True
for i in range(num):
	a = set(map(int,input().split(' ')))
	lis.append(a)
	if a.difference(set_val) != set() or len(a) >= len(set_val):
		val = False
print(val)
