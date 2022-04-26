n=int(input())
for i in range(1,n+1):
    x=int(input())
    fact=1
    for j in range(1,x+1):
        fact=fact*j
    print(fact)