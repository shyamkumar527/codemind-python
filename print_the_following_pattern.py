n=int(input())
a=0
for i in range(n):
    if i==0:
        print("*")
    elif i==n-1:
        for j in range(n):
            print("*",end="")
    else:
        print("*",end="")
        j=1
        while(1):
            if j==a:
                print("*")
                break
            else:
                print(" ",end="")
            j+=1
    a+=1