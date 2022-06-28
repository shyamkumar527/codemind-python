n=int(input())
a=0
if n>0:
    while n!=1:
        if n%2==0:
            n//=2
        elif n%3==0:
            n//=3
        elif n%5==0:
            n//=5
        else:
            a=1
            print('Not Ugly Number')
            break
    if a==0:
        print('Ugly Number')
else:
    print('Not Ugly Number')