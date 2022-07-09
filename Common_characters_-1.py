s=input()
a=s.lower()
w=ans=0
l=[]
for i in a.split():
    w+=1
    l.append(i)
for i in l[0]:
    c=0
    for j in range(w):
        if i in l[j]:
            c+=1
    if c==w:
        print(i,end='')
        ans=1
if ans==0:
    print('-1')