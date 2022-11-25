r,c=map(int,input().split())
arr=[]
for i in range(r):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(c):
    m=-10000
    for j in range(r):
        if arr[j][i]>m:
            m=arr[j][i]
    print(m)