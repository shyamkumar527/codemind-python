n=int(input())
arr=list(map(int,input().split()))
ans=0
a=n
for i in range(n):
    a-=1
    if arr[i]==1:
        ans+=pow(2,a)
print(ans)