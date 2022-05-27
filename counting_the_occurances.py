s=input()
x=input()
if x not in s:
    print('-1')
else:
    c=0
    for i in s:
        if i==x:
            c+=1
    print(c)