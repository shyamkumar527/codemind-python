def rev(n):
    ans=0
    while n:
        r=n%10
        ans=(ans*10)+r
        n//=10
    return ans
    
def palin(n):
    p=n
    pa=0
    while p:
        r=p%10
        pa=(pa*10)+r
        p//=10
    if pa==n:
        return 1
    return 0

x=int(input())
while 1:
    x=x+rev(x)
    if(palin(x)==1):
        print(x)
        break
    