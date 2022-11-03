s1=input()
s2=input()
c=0
a=s1.lower()
b=s2.lower()
l1=a.split()
l2=b.split()
for i in l1:
    if l1.count(i)==1:
        if i in l2 and l2.count(i)==1:
            c+=1
print(c)