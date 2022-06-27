n=int(input())
s=0
pro=1
while n:
    r=n%10
    s+=r
    pro*=r
    n//=10
if s==pro:
    print('Spy Number')
else:
    print('Not Spy Number')