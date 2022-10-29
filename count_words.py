s=input()
m=s.split()
c=0
v="AEIOUaeiou"
for i in m:
    if i[0] in v and i[-1] not in v:
        c+=1
print(c)