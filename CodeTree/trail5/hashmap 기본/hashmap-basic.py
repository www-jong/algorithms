n = int(input())
commands = []
d={}
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
        d[k]=v
    else:
        if cmd=='remove':
            del d[k]
        else:
            print(d[k] if k in d else 'None')

# Please write your code here.
