s=input()
val=0
v="QWERTYUIOPASDFGHJKLZXCVBNM"
for i in s:
    if i in v:
        val+=1
print(val)