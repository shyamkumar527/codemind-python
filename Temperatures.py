n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    ans=0
    for j in range(i+1,n):
        ans+=1
        if arr[i]<arr[j]:
            print(ans,end=' ')
            break
    else:
        print('0',end=' ')