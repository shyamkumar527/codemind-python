n=int(input())
l=[]
a=0
while n:
    r=n%10
    if r not in l:
        l.append(r)
    else:
        a=1
        break
    n//=10
if a==0:
    print('Unique Number')
else:
    print('Not Unique Number')