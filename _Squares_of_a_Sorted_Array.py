n=int(input())
arr=list(map(int,input().split()))
arr1=list()
for i in arr:
    x=i*i
    arr1.append(x)
arr1.sort()
for i in arr1:
    print(i,end=' ')