from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    d=defaultdict(int)
    d2=defaultdict(int)
    for i in range(len(friends)):
        d2[friends[i]]=i
    li=[[0]*len(friends) for _ in range(len(friends))]
    visit=[[0]*len(friends) for _ in range(len(friends))]
    r=[0]*len(friends)
    
    for i in gifts:
        a,b=i.split()
        print(a,b,li[d2[a]][d2[b]])
        li[d2[a]][d2[b]]+=1
        d[a]+=1
        d[b]-=1
    for i in li:
        print(i)
        
    for i in range(len(friends)):
        for j in range(len(friends)):
            c=0
            if li[i][j] and not visit[i][j]:
                if li[i][j]>li[j][i]:
                    print(f'1, {i}-{j},   {i},{j}')
                    r[i]+=1
                    c=1
                elif li[j][i]>li[i][j]:
                    print(f'2, {j}-{i},   {i},{j}')
                    r[j]+=1
                    c=1
                else:
                    if d[friends[i]]>d[friends[j]]:
                        print(f'3, {i}-{j},   {i},{j}')
                        r[i]+=1
                        c=1
                    elif d[friends[i]]<d[friends[j]]:
                        print(f'4, {j}-{i},   {i},{j}')
                        r[j]+=1
                    c=1
            elif not visit[i][j] and (li[i][j]==li[j][i]):
                if d[friends[i]]>d[friends[j]]:
                    print(f'3, {i}-{j},   {i},{j}')
                    r[i]+=1
                    c=1
                elif d[friends[i]]<d[friends[j]]:
                    print(f'4, {j}-{i},   {i},{j}')
                    r[j]+=1
                    c=1
            if c:
                visit[i][j]=1
                visit[j][i]=1
    print(d)
    print(r)
    for i in visit:
        print(i)
    return max(r)