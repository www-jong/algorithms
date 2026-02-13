N=int(input())
d={ 'STRAWBERRY':0,'BANANA':0,'LIME':0,'PLUM':0}
for _ in range(N):
    word,c=input().split()
    d[word]+=int(c)
print('YES' if 5 in d.values() else 'NO')