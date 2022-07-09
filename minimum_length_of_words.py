s=input()
l=100
for i in s.split():
    le=len(i)
    if le<l:
        l=le
print(l)