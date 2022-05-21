n=int(input())
x=n-1
y=0
arr=list(map(int,input().split()))
arr1=list()
for i in range(n):
    if x>=n/2:
        arr1.append(arr[x])
        x-=1
    else:
        arr1.append(arr[y])
        y+=1
for i in range(n):
    print(arr1[i],end=' ')