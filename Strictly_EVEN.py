n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    if arr[i]%2==0:
        if i%2!=0:
            ans+=1
            print('False')
            break
if ans==0:
    print('True')