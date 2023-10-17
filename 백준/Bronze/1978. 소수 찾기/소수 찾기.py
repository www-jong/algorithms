input();n=map(int,input().split());count=0;
for i in n:
    ch=0
    for j in range(2,i//2+1):
        if i%j==0:
            ch=1
            break
    if ch==0 and i!=1:
        count+=1
print(count)