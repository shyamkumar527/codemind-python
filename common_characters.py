s1=input()
s2=input()
l=[]
c=0
v="abcdefghijklmnopqrstuvwxyz"
for i in s2.lower():
    if i in s1.lower():
        l.append(i)
        c=1
for i in v:
    if i in l:
        print(i,end="")
if c==0:
    print("-1")