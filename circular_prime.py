def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+2):
            if n%i==0:
                return 0
        else:
            return 1
    else:
        return 0
n=int(input())
a=prime(n)
rev=0
while n:
    r=n%10
    rev=(rev*10)+r
    n//=10
b=prime(rev)
if a==1 and b==1:
    print('circular prime')
elif a==1 and b!=1:
    print('prime but not a circular prime')
else:
    print('not prime')