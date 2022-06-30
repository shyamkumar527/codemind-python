n=int(input())
arr=list(map(int,input().split()))
l=[]
ans=c=0
for i in arr:
    if i not in l:
        l.append(i)
        x=arr.count(i)
        if x==i:
            ans+=i
            c+=1
if c>0:
    res=ans/c
    print('%.2f' %res)
else:
    print('-1')