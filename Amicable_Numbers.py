m=int(input())
n=int(input())
s1=s2=0
for i in range(1,(m//2)+1):
    if m%i==0:
        s1+=i
for i in range(1,(n//2)+1):
    if n%i==0:
        s2+=i
if m==s2 and n==s1:
    print('Amicable')
else:
    print('Not Amicable')