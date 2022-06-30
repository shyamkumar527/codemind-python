n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
c=0
for i in arr:
    if (i<a or i>b) and i not in l:
        l.append(i)
        c=1
if c==0:
    print('-1')
else:
    print(max(l))