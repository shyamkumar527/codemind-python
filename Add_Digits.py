n=int(input())
while 1:
    if n<10:
        print(n)
        break
    else:
        x=0
        while n:
            r=n%10
            x+=r
            n//=10
        n=x