from itertools import permutations
N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
li=[]
for i in permutations([1,2,3,],3):
    tmp={(i[0],i[1]),(i[1],i[2]),(i[2],i[0])}
    li.append(tmp)
answer=0
for i in li:
    tmp=0
    for j in moves:
        if j in i:
            tmp+=1
    answer=max(answer,tmp)
print(answer)