n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    x=arr.count(i)
    if x==i and i not in l:
        l.append(i)
        c=1
        print(i,end=' ')
if c==0:
    print('-1')