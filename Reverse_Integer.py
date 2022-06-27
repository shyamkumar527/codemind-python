n=int(input())
ans=s=0
if n<0:
    s=1
    n*=-1
while n:
    r=n%10
    ans=(ans*10)+r
    n//=10
if s==1:
    print(ans*-1)
else:
    print(ans)