n=int(input())
x=n
c=0
while x:
    c+=1
    x//=10
pro=n**2
rev=ans=0
for i in range(c):
    r=pro%10
    rev=(rev*10)+r
    pro//=10
while rev:
    r=rev%10
    ans=(ans*10)+r
    rev//=10
if ans==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')