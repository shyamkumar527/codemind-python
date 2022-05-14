def perf(n):
    a=1
    while a<n:
        sq=a*a
        if(sq==n):
            return 1
        a+=1
    return 0
        
n=int(input())
for i in range(n):
    a=int(input())
    if(perf(a)):
        print("True")
    else:
        print("False")