n=int(input())
arr=list(map(int,input().split()))
arr1=list()
for i in arr:
    if i not in arr1:
        arr1.append(i)
for i in arr1:
    print(i,end=' ')