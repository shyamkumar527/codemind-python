n=int(input())
arr=list(map(int,input().split()))
ans=1
for i in range(0,n-2,2):
    if (arr[i]<arr[i+1] and arr[i+2]<arr[i+1]) or (arr[i]>arr[i+1] and arr[i+2]>arr[i+1]):
        ans=1
    else:
        ans=0
        print('no')
        break
if ans==1:
    print('yes')