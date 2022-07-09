s=input()
c=0
l=[]
for i in s.split():
    l.append(i[::-1])
    c+=1
for i in range(c):
    print(l[i],end=' ')