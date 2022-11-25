n=int(input())
c=0
for i in range(2,(n//2)+1):
    if n%i==0:
        c+=1
        break
if c==0:
    d=0
    p=0
    while n:
        r=n%10
        n=n//10
        d+=1
        if r==2 or r==3 or r==5 or r==7:
            p+=1
    if p==d:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')