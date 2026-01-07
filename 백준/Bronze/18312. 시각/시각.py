n,K=input().split()
a=[str(i).zfill(2) for i in range(60)]
res=0
for i in a[:int(n)+1]:
    for j in a:
        for k in a:
            if K in i+j+k:res+=1
print(res)