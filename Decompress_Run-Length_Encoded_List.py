n=int(input())
arr=list(map(int,input().split()))
res=list()
for i in range(0,n,2):
    x=arr[i+1]
    for j in range(arr[i]):
        res.append(x)
for i in res:
    print(i,end=' ')