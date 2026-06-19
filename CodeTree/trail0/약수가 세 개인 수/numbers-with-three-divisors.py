start, end = map(int, input().split())
r=0
for i in range(start,end+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
        if c>3:
            break
    if c==3:
        r+=1

print(r)