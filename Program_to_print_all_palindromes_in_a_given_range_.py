def palin(n):
    x=n
    rev=0
    while x:
       r=x%10
       rev=(rev*10)+r
       x=x//10
    if(rev==n):
        return 1
    else:
        return 0
        
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(palin(i)):
        print(i,end=" ")