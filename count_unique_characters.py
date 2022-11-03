s=input()
d={}
c=0
for i in s.lower():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i in d and d[i]==1:
        c+=1
print(c)