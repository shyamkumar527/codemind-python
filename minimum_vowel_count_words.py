s=input()
v="AEIOUaeiou"
l=s.split()
ans=1000
val=0
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    if c<ans:
        ans=c
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    if c==ans:
        val+=1
print(val)