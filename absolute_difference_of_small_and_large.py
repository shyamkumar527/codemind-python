s=input()
l=s.split()
for i in l:
    h=0
    l=200
    for j in i:
        if ord(j)>h:
            h=ord(j)
        if ord(j)<l:
            l=ord(j)
    print(h-l,end=" ")