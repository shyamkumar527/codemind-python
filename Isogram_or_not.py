s=input()
c=0
l=[]
for i in s:
    if i not in l:
        l.append(i)
    else:
        c=1
        break
if c==0:
    print('True')
else:
    print('False')