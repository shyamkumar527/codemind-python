s=input()
d={}
v="qwertyuiopasdfghjklzxcvbnm"
for i in s.lower():
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
print(len(d))