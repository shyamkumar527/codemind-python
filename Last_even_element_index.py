n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    if arr[i]%2==0:
        ans=i
print(ans)