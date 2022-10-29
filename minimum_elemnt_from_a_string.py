s=input()
l=list(s.split())
for i in l:
    j=i
m=min(j)
if m.lower() in j:
    print(m.lower())
else:
    print(m)