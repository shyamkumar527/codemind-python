s=input()
v=c=d=w=0
vow='aeiouAEIOU'
dig='0123456789'
for i in s:
    if i in vow or i in vow:
        v+=1
    elif i in dig:
        d+=1
    elif i==' ':
        w+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)