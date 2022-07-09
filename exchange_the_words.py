s=input()
c=0
l=[]
for i in s.split():
    l.append(i)
    c+=1
for i in range(c-1,-1,-1):
    print(l[i],end=' ')