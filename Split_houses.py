n=int(input())
s=input()
b=""
ans=1
for i in range(n-1):
    if s[i]=="H" and s[i+1]=="H":
        ans=0
        break
for i in range(n):
    if s[i]=="H":
        b+="H"
    else:
        b+="B"
if ans==1:
    print("YES")
    print(b)
else:
    print("NO")