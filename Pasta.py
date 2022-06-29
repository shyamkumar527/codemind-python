m,n=map(int,input().split())
a=0
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
for i in brr:
    if i in arr:
        arr.remove(i)
    else:
        a=1
        break
if a==0:
    print('Yes')
else:
    print('No')