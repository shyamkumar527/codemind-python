n=int(input())
arr=list(map(int,input().split()))
ans=1
for i in range(n-1):
    if arr[i]>=arr[i+1]:
        ans=0
        break
if ans==1:
    print('yes')
else:
    print('no')