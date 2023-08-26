t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    for j in range(k,1,-1):
        s=s[j-1::-1]+s[j:]
    print(s)