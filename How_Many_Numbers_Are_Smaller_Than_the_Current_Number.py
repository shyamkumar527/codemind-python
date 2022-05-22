n=int(input())
arr=list(map(int,input().split()))
new=list()
for i in range(n):
    count=0
    for j in range(n):
        if arr[i]>arr[j]:
            count+=1
    new.append(count)
for i in new:
    print(i,end=' ')