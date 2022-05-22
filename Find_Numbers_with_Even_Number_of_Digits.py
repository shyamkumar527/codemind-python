n=int(input())
arr=list(map(int,input().split()))
res=0
for i in arr:
    c=0
    while i:
        c+=1
        i//=10
    if c%2==0:
        res+=1
print(res)