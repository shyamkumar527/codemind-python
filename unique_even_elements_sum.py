n=int(input())
arr=list(map(int,input().split()))
l=[]
ans=0
for i in arr:
    if i not in l:
        l.append(i)
        if i%2==0:
            ans+=i
print(ans)