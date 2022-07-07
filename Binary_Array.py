n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in arr:
    if i!=0 and i!=1:
        print('False')
        ans=1
        break
if ans==0:
    print('True')