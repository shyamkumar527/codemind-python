n=int(input())
x=n
res=0
while x:
    pro=1
    r=x%10
    for i in range(1,r+1):
        pro=pro*i
    res+=pro
    x//=10
if res==n:
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')