n=int(input())
arr=list(map(int,input().split()))
ans=su=0
for i in arr:
    su+=i
avg=su//n
for i in range(n):
    if arr[i]==avg:
        ans=1
        break
if ans==1:
    print('True')
else:
    print('False')