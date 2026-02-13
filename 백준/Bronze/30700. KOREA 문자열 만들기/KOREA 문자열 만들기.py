S=input()
r=0
idx=0
tmp='KOREA'
for i in S:
    if i==tmp[idx]:
        r+=1
        if idx==4:
            idx=0
            continue
        idx+=1
print(r)