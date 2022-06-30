n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(1,n,2):
    for j in range(arr[i]):
        l.append(arr[i-1])
for i in l:
    print(i,end=' ')