n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    x=arr.count(i)
    if x==i and i not in l:
        c=1
        l.append(i)
if c==0:
    print('-1')
else:
    mi=min(l)
    ma=max(l)
    print(mi,ma)