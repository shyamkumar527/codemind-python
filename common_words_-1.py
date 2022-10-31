s1=input()
s2=input()
c=0
c1=s1.lower()
c2=s2.lower()
l1=c1.split()
l2=c2.split()
for i in l1:
    if i in l2:
        c+=1
print(c)