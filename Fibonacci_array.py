n=int(input())
arr=list(map(int,input().split()))
ans=1
if n<3:
    print('no')
else:
    for i in range(n-2):
        if arr[i+2]!=arr[i]+arr[i+1]:
            ans=0
            print('no')
            break
    if ans==1:
        print('yes')