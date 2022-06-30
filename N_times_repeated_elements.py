n=int(input())
arr=list(map(int,input().split()))
k=int(input())
l=[]
c=0
for i in arr:
    x=arr.count(i)
    if x==k and i not in l:
        l.append(i)
        c=1
if c==0:
    print('-1')
else:
    for i in l:
        print(i,end=' ')