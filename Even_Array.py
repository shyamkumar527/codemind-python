n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in arr:
    if i%2!=0:
        ans+=1
        print('False')
        break
if ans==0:
    print('True')