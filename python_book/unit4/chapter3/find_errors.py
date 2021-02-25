""" This code is a solution of errors in the code in comments."""
# c = dict()
# n=input(Enter total number)
# i=1
# while i<=n
# a = input("Enter place")
# b = input("Enter number")
# c(a) = b
# i+=1
# print("place",'\t',"number")
# for i in c:
# print(i,"\t",cla[i])

c = dict()
n = int(input("Enter total numbers"))
i = 1
while i<= n:
    a = input("Enter place ")
    b = input("Enter number ")
    c[a] = b
    i+=1
print("place","\t","number")
for i in c:
    print(i,'\t',c[i])
