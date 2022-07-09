s=input()
l=[]
c=0
for i in s.split():
    l.append(i)
    c+=1
print(min(l[0]),end=' ')
print(max(l[c-1]),end=' ')