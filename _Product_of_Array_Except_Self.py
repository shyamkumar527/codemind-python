n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    val=1
    for j in range(n):
        if i!=j:
            val*=arr[j]
    print(val,end=' ')