n=int(input())
for i in range(n,0,-1):
    x=chr(i+64)
    for j in range(1,i+1):
        print(x,end=' ')
    print()