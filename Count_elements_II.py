m,n=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    if i not in brr and i not in l:
        c+=1
        l.append(i)
for i in brr:
    if i not in arr and i not in l:
        c+=1
        l.append(i)
print(c)