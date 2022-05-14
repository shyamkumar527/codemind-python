def palin(n):
    x=n
    rev=0
    while x:
        r=x%10
        rev=(rev*10)+r
        x=x//10
    if rev==n:
        return 1
    else:
        return 0
        
n=int(input())
for i in range(n):
    a=int(input())
    if a<0:
        print("False")
    else:
        if(palin(a)):
            print("True")
        else:
            print("False")