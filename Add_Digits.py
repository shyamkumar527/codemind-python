n=int(input())
x=n
while True:
    sum=0
    if x<10:
        print(x)
        break
    else:
        while x:
            r=x%10
            sum+=r
            x//=10
            if(x==0):
                x=sum
                break