def palin(n):
    rev=0
    x=n
    while x:
        r=x%10
        rev=(rev*10)+r
        x//=10
    if rev==n:
        return 1
    return 0
n=int(input())
d=1
a=0
while True:
    if(palin(n-d)):
        a=1
        print(n-d,end=' ')
    if(palin(n+d)):
        a=1
        print(n+d)
    if a==1:
        break
    else:
        d+=1