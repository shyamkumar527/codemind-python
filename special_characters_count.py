s=input()
l=s.split()
val=0
v="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLXCVBNM1234567890"
for i in l:
    for j in i:
        if j not in v:
            val+=1
print(val)