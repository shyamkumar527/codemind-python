n=int(input())
arr=list(map(int,input().split()))
new=list()
for i in range(n):
    if i==n-1:
        new.append(-1)
    else:
        ma=0
        for j in range(i+1,n):
            if arr[j]>ma:
                ma=arr[j]
        new.append(ma)
for i in new:
    print(i,end=' ')