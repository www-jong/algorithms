import sys
tmp=sys.stdin.readlines()
li=[]
for i in tmp:
    for j in i.split():
        li.append(int(j[::-1]))
print(*sorted(li[1:]),sep="\n")