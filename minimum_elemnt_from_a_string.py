s=input()
l=[]
c=0
for i in s.split():
    l.append(i)
    c+=1
ans=min(l[c-1])
if (ans.lower()) in s:
    print(ans.lower())
else:
    print(ans)