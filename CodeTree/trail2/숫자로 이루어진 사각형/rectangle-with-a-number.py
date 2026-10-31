n = int(input())

cnt=0
idx=1
for i in range(1,n*n+1):
    print(idx,end=' ')
    cnt+=1
    idx+=1
    if cnt==n:
        print()
        cnt=0
    if idx==10:
        idx=1