n=int(input())
x=n
for i in range(1,n+1):
    for j in range(1,x+1):
        print(j,end='')
    x=x-1
    print('')