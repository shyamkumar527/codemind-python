n=int(input())
a=0
for i in range(n//2):
    if i*i==n:
        a=1
        break
if a==1:
    print('True')
else:
    print('False')