s=input()
d={}
c=0
for i in s.lower():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in s.lower():
    if d[i]==1:
        print(i)
        c=1
        break
if c==0:
    print("-1")