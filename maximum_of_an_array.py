n=int(input())
arr=list(map(int,input().split()))
ans=-100
for i in arr:
    if i>ans:
        ans=i
print(ans)