n=int(input())
l=[0,1]
a=0
b=1
for i in range(n):
    c=a+b
    l.append(c)
    a=b
    b=c
low=high=0
for i in l:
    if i<n:
        low=i
    if i>n:
        high=i
        break
if((n-low)==(high-n)):
    print(low,high)
elif((n-low)<(high-n)):
    print(low)
else:
    print(high)