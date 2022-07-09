s=input()
a=s.lower()
c=0
for i in a.split():
    if i==i[::-1]:
        c+=1
print(c)