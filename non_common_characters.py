s1=input()
s2=input()
l=[]
v="abcdefghijklmnopqrstuvwxyz"
for i in s2.lower():
    if i not in s1.lower():
        l.append(i)
for i in s1.lower():
    if i not in s2.lower():
        l.append(i)
for i in v:
    if i in l:
        print(i,end="")