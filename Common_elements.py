m,n=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
l=[]
for i in arr:
    if i in brr and i not in l:
        l.append(i)
for i in brr:
    if i in arr and i not in l:
        l.append(i)
for i in l:
    print(i,end=' ')