n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
ans=0
for i in arr:
    if i>=a and i<=b:
        ans+=i
print(ans)