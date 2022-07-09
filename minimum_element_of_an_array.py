n=int(input())
arr=list(map(int,input().split()))
ans=1000
for i in arr:
    if i<ans:
        ans=i
print(ans)