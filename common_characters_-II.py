s1=input()
s2=input()
c=0
l=[]
for i in s1.lower():
    if i in s2.lower() and i not in l and i!=" ":
        l.append(i)
        c+=1
print(c)