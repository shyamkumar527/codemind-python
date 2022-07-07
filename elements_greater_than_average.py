n=int(input())
arr=list(map(int,input().split()))
sum=ans=0
for i in range(n):
    sum+=arr[i]
avg=sum//n
for i in arr:
    if i>=avg:
        ans+=1
print(ans)