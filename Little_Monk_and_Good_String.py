s=input()
vow='aeiou'
count=0
ma=0
for i in s:
    if i in vow:
        count+=1
    else:
        if count>ma:
            ma=count
        count=0
if count>ma:
    ma=count
print(ma)