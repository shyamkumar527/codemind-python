def prime(n):
    if n<2:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
a=b=n
t=0
while(1):
    if(prime(a)):
        print(t)
        break
    if(prime(b)):
        print(t)
        break
    t+=1
    a-=1
    b+=1