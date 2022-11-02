s=input()
l=s.split()
for i in range(len(l)-1,-1,-1):
    x=l[i]
    print(x[-1::-1],end=" ")