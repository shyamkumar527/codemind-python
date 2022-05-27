s=input()
t=list()
allow=0
for i in s:
    if i not in t:
        t.append(i)
for i in t:
    count=0
    for j in range(0,len(s)):
        if s[j]==i:
            count+=1
    if count%2!=0:
        allow+=1
if allow<2:
    print('Valid String')
else:
    print('Not Valid')