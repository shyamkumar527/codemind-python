n=int(input())
arr=[]
s=0
a=n-1
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(n):
    for j in range(n):
        if i==j or j==a:
            s+=arr[i][j]
    a-=1
print(s)