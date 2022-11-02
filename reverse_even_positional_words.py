s=input()
l=s.split()
for i in range(len(l)):
    if i%2==0:
        x=l[i]
        print(x[-1::-1],end=" ")
    else:
        print(l[i],end=" ")