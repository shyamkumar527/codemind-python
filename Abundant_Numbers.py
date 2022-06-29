n=int(input())
ans=0
for i in range(1,(n//2)+2):
    if n%i==0:
        ans+=i
if ans>n:
    print('True')
else:
    print('False')