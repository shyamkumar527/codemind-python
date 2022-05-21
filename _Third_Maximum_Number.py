n=int(input())
n1=n2=n3=-1
arr=list(map(int,input().split()))
for i in arr:
    if i>n1:
        n1=i
for i in arr:
    if i!=n1 and i>n2:
        n2=i
for i in arr:
    if i!=n1 and i!=n2 and i>n3:
        n3=i
if n1>-1 and n2>-1 and n3>-1:
    print(n3)
else:
    print(n1)