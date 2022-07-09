n=int(input())
arr=list(map(int,input().split()))
x=int(input())
ans=0
for i in range(n):
    if arr[i]==x:
        ans=1
        break
if ans==1:
    print('True')
else:
    print('False')