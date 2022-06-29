n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    c=0
    x=arr[i]
    if x<0:
        x*=-1
    while x:
        c+=1
        x//=10
    if arr[i]==0:
        print('1',end=' ')
    else:
        print(c,end=' ')