x,y=map(int,input().split())
a=x
b=y
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
gcd=a
lcm=(x*y)//gcd
print(lcm)