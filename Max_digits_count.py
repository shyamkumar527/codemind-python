n=int(input())
arr=list(map(int,input().split()))
dig=0
ans=0
for i in range(n):
    x=arr[i]
    c=0
    while x:
        c+=1
        x//=10
    if c>dig:
        dig=c
for i in range(n):
    x=arr[i]
    c=0
    while x:
        c+=1
        x//=10
    if c==dig:
        ans+=1
print(ans)