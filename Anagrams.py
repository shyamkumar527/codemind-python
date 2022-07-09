s1=input()
s2=input()
l1=list(s1.lower())
l2=list(s2.lower())
l1.sort()
l2.sort()
if l1==l2:
    print('True')
else:
    print('False')