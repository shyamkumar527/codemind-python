for i in range(int(input())):
    n=int(input())
    c=0
    arr=list(map(int,input().split()))
    for j in arr:
        if j%2==1:
            c+=1
    if c%2==1:
        c-=1
    print(c//2)