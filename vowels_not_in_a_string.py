s=input()
ans=0
if 'a' not in s:
    print('a',end=' ')
    ans=1
if 'e' not in s:
    print('e',end=' ')
    ans=1
if 'i' not in s:
    print('i',end=' ')
    ans=1
if 'o' not in s:
    print('o',end=' ')
    ans=1
if 'u' not in s:
    print('u',end=' ')
    ans=1
if ans==0:
    print('0')