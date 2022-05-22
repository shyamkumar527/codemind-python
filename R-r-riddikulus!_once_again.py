a,b=map(int,input().split())
arr=list(map(int,input().split()))
new=list()
for i in range(a):
    ind=(i-b)
    if ind<0:
        ind+=a
    new.insert(ind,arr[i])
for i in new:
    print(i,end=' ')