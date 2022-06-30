def palin(n):
    x=n
    rev=0
    while x:
        r=x%10
        rev=(rev*10)+r
        x//=10
    if rev==n:
        return 1
    return 0
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(palin(i)):
        c+=1
print(c)