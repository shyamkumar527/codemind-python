n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in arr:
    if i%2!=0:
        break
    else:
        ans+=i
print(ans)