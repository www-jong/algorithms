N,C,W=map(int,input().split())
li=[int(input()) for _ in range(N)]
r=0
for i in range(1,max(li)+1):
    w=0
    c=0
    for j in li:
        wt=j//i*W*i
        ct=(j//i+(0 if j%i else -1))*C
        if wt-ct>0:
            w+=wt
            c+=ct
    r=max(r,w-c)
print(r)