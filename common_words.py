s1=input()
s2=input()
for i in s2.lower().split():
    if i in s1.lower().split():
        print(i,end=" ")