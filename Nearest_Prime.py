def prime(n):
    if n<2:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
for i in range(int(input())):
    n=int(input())
    x=n
    y=n
    while(1):
        if(prime(x)):
            print(x)
            break
        if(prime(y)):
            print(y)
            break
        x-=1
        y+=1