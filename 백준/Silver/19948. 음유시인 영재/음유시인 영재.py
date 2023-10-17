S=input().rstrip()
title=''.join([i[0].upper() for i in S.split()])
S+=title+'.'

space=int(input())
check=list(map(int,input().split()))
res=0
for i in range(len(S)-1):
    if S[i]==S[i+1]:continue

    g=(ord(S[i])-97 if ord(S[i])>=97 else ord(S[i])-65)

    if S[i]==" ":
        if space:
            space-=1
        else:
            print(-1)
            exit()
        continue
    if check[g]==0:
        print(-1)
        exit()
    else:
        check[g]-=1
print(title)