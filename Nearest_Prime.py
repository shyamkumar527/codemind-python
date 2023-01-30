def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
    
for i in range(int(input())):
    n=int(input())
    a=n
    b=n
    while(1):
        if(prime(a)):
            print(a)
            break
        if(prime(b)):
            print(b)
            break
        a-=1
        b+=1