n=int(input())
x=0
a=0
for i in range(n,0,-1):
    x+=1
    for j in range(1,i+1):
        print(x,end=' ')
        x+=1
    a+=1
    x=a
    print()