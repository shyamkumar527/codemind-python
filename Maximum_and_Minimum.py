n=int(input())
val=c=0
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i==arr.count(i):
        l.append(i)
        c=1
if c!=0:
    print(min(l),max(l))
else:
    print("-1")