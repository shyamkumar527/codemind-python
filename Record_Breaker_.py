t=int(input())
loop=0
for i in range(t):
    loop+=1
    n=int(input())
    c=0
    arr=list(map(int,input().split()))
    for j in range(n):
        ans1=ans2=-1
        if j==0:
            if arr[j]>arr[j+1]:
                c+=1
        else:
            for k in range(j):
                if arr[k]>arr[j]:
                    ans1=1
                    break
                elif arr[k]<arr[j]:
                    ans1=0
            if j==(n-1):
                if ans1==0:
                    c+=1
            else:
                if arr[j]>arr[j+1]:
                    ans2=1
                if ans1==0 and ans2==1:
                    c+=1
    print('Case #',end='')
    print(loop,end='')
    print(':',end=' ')
    print(c)