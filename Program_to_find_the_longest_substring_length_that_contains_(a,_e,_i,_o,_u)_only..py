s=input()
c=m=0
vow='aeiou'
for i in s:
    if i in vow:
        c+=1
    else:
        if c>m:
            m=c
            c=0
if c>m:
    m=c
print(m)