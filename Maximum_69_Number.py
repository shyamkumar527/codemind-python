n=int(input())
x=n
rev=0
ans=a=0
while x:
    r=x%10
    rev=(rev*10)+r
    x=x//10
while rev:
    r=rev%10
    if r==6 and a==0:
        r=9
        a+=1
    ans=(ans*10)+r
    rev=rev//10
print(ans)