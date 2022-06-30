n=int(input())
arr=list(map(int,input().split()))
l=[]
ans=0
for i in arr:
    x=arr.count(i)
    if x==i and i not in l:
        l.append(i)
        ans+=1
print(ans)