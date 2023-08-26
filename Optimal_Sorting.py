t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for j in range(1,n):
        if(l[j-1]>l[j]):
            f=1
            break
    if f==0:
        print(0)
    else:
        print(max(l)-min(l))