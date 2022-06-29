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
if(palin(n)):
    print('True')
else:
    print('False')