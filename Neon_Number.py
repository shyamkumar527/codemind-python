n=int(input())
x=n
n=n*n
s=0
while n:
    r=n%10
    s+=r
    n//=10
if s==x:
    print('Neon Number')
else:
    print('Not Neon Number')