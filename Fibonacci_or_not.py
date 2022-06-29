n=int(input())
ans=0
a=0
b=1
while True:
    c=a+b
    if c==n:
        a=1
        break
    elif c>n:
        break
    a=b
    b=c
if a==1:
    print('True')
else:
    print('False')