n=int(input())
a=n-1
b=0
for i in range(n):
    for j in range(n):
        if j==b or j==a:
            print("x",end="")
        else:
            print("0",end="")
    a-=1
    b+=1
    print()