s=input()
val=0
v="qwertyuiopasdfghjklzxcvbnm"
for i in s:
    if i in v:
        val+=1
print(val)