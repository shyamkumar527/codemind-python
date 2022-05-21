alice=bob=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(3):
    if a[i]>b[i]:
        alice+=1
    elif a[i]<b[i]:
        bob+=1
print(alice,bob)