n=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
x=max(d.values())
c=0
for i in d:
    if d[i]==x:
        c+=1
if c==1:
    for i in d:
        if d[i]==x:
            print(i)
            break
else:
    ans=100000
    for i in d:
        if d[i]==x:
            if i<ans:
                ans=i
    print(ans)