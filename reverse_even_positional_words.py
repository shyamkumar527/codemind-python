s=input()
c=0
for i in s.split():
    if c%2==0:
        print(i[::-1],end=' ')
        c+=1
    else:
        print(i,end=' ')
        c+=1