R,C=map(int,input().split())
li=[input() for i in range(R)]
words=[]
for i in range(R):
    for j in range(C):
        if j-1<0 or li[i][j-1]=='#':
            tmp=''
            for k in range(j,C):
                if li[i][k]=='#':break
                tmp+=li[i][k]
            if len(tmp)>=2:
                words.append(tmp)
for i in range(C):
    for j in range(R):
        if j-1<0 or li[j-1][i]=='#':
            tmp=''
            for k in range(j,R):
                if li[k][i]=='#':break
                tmp+=li[k][i]
            if len(tmp)>=2:
                words.append(tmp)

print(sorted(words)[0])