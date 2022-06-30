n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
ans=0
c=0
for i in arr:
    if i>=a and i<=b:
        if i>ans:
            c=1
            ans=i
if c==1:
    print(ans)
else:
    print('-1')