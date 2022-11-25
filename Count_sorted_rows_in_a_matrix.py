n,m=map(int,input().split())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
c=0
for i in range(n):
    ans=1
    if arr[i][0]<arr[i][1]:
        d=1
    elif arr[i][0]>arr[i][1]:
        d=-1
    else:
        if arr[i][1]<arr[i][2]:
            d=1
        elif arr[i][1]>arr[i][2]:
            d=-1
    for j in range(m-1):
        if d==1:
            if arr[i][j]>arr[i][j+1]:
                ans=0
                break
        elif d==-1:
            if arr[i][j]<arr[i][j+1]:
                ans=0
                break
    if ans==1:
        c+=1
print(c)