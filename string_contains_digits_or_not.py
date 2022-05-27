t=int(input())
for i in range(t):
    s=input()
    for j in s:
        if j.isdigit():
            print('Yes')
            break
    else:
        print('No')