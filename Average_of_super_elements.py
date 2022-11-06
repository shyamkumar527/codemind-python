n=int(input())
val=c=0
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i not in l:
        if i==arr.count(i):
            val+=i
            c+=1
        l.append(i)
if c!=0:
    print('%.2f' %(val/c))
else:
    print("-1")