t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    if s==s[::-1] and l%2==0:
        print('YES EVEN')
    elif s==s[::-1] and l%2!=0:
        print('YES ODD')
    else:
        print('NO')