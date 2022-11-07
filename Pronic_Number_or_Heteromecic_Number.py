n=int(input())
ans=0
for i in range(n//2):
    if i*(i+1)==n:
        ans=1
        break
if ans==1:
    print("YES")
else:
    print("NO")