n=int(input())
arr=list(map(int,input().split()))
l=[]
ans=[]
for i in arr:
    if i not in l:
        l.append(i)
        ans.append(i)
        x=arr.count(i)
        ans.append(x)
print(*ans)