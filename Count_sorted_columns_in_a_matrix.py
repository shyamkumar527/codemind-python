n,m=map(int,input().split())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
c=0
for i in range(m):
    ans=1
    if arr[0][i]<arr[1][i]:
        d=1
    elif arr[0][i]>arr[1][i]:
        d=-1
    else:
        if arr[1][i]<arr[2][i]:
            d=1
        elif arr[1][i]>arr[2][i]:
            d=-1
    for j in range(n-1):
        if d==1:
            if arr[j][i]>arr[j+1][i]:
                ans=0
                break
        elif d==-1:
            if arr[j][i]<arr[j+1][i]:
                ans=0
                break
    if ans==1:
        c+=1
print(c)