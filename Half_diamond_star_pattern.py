n=int(input())
if 3<=n and n<=100:
    a=1
    for i in range(n):
        for j in range(a):
            print("*",end="")
        print()
        a+=1
    a=n-1
    for i in range(n-1,0,-1):
        for j in range(a):
            print("*",end="")
        print()
        a-=1
else:
    print("The pattern is not possible")