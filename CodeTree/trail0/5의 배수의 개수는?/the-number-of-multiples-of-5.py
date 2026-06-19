li=[list(map(int,input().split())) for _ in range(4)]
r=0
for i in li:
    for j in i:
        if j%5==0:
            r+=1
print(r)