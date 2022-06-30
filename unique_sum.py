n=int(input())
arr=list(map(int,input().split()))
res=0
l=[]
for i in range(n):
    if arr[i] not in l:
        l.append(arr[i])
        res+=arr[i]
print(res)