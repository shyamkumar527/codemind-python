s=input()
ans=0
v="AEIOUaeiou"
l=[]
for i in s:
    if i in v and i not in l:
        l.append(i)
if len(l)>0:
    ans=1
    print(*l)
if ans==0:
    print("-1")