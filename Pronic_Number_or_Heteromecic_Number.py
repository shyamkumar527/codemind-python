n=int(input())
a=0
for i in range((n//2)+1):
    if i*i+1==n:
        a=1
        break
if a==1:
    print('NO')
else:
    print('YES')