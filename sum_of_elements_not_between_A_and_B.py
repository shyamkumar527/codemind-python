n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
ans=0
for i in arr:
    if (i<a or i>b) and i not in l:
        l.append(i)
        ans+=i
print(ans)