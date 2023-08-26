t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for j in range(1,n):
        if l[j]<l[j-1]:
            f=1
            break
    if f==1:
        print(max(l)-min(l))
    else:
        print(0)