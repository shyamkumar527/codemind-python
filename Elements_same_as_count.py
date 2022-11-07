n=int(input())
arr=list(map(int,input().split()))
l=[]
ans=0
for i in arr:
    if i not in l:
        l.append(i)
        if arr.count(i)==i:
            print(i,end=" ")
            ans=1
if ans==0:
    print("-1")