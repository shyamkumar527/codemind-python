s=input()
l=s.split()
ans=0
for i in l:
    x=i[-1::-1]
    if(x.lower()==i.lower()):
        ans+=1
print(ans)