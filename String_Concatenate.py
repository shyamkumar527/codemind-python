a=input()
b=input()
c=a+b
dig=65
for i in range(70):
    for j in range(len(c)):
        if ord(c[j])==dig:
            print(c[j],end='')
    dig+=1