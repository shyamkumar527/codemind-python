n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    c=a=0
    if arr[i]<0:
        a=1
        arr[i]*=-1
    x=arr[i]
    while x:
        c+=1
        x//=10
    if a==1:
        arr[i]*=-1
    if c==k:
        ans+=1
    if k==1 and arr[i]==0:
        ans+=1
print(ans)