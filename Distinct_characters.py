s=input()
d={}
v="abcdefghijklmnopqrstuvwxyz"
for i in s.lower():
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
for i in v:
    if i in d:
        print(i,end="")