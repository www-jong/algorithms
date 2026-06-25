import bisect
def solution(info, query):
    answer = []
    def get(a,b,c,d,e):
        try:
            if dic[a][b][c][d][0]==0:
                dic[a][b][c][d][1].sort()
                dic[a][b][c][d][0]=1
            return len(dic[a][b][c][d][1])-bisect.bisect_left(dic[a][b][c][d][1],e)
        except:
            return 0

    def func(a,b,c,d,e,idx):
        if idx==4:
            return get(a,b,c,d,e)
        tmp=0
        try:
            if idx==0 and a=='-':
                for i in dic.keys():
                    tmp+=func(i,b,c,d,e,idx+1)
            elif idx==1 and b=='-':
                for i in dic[a].keys():
                    tmp+=func(a,i,c,d,e,idx+1)
            elif idx==2 and c=='-':
                for i in dic[a][b].keys():
                    tmp+=func(a,b,i,d,e,idx+1)
            elif idx==3 and d=='-':
                for i in dic[a][b][c].keys():
                    tmp+=func(a,b,c,i,e,idx+1)
            else:
                tmp+=func(a,b,c,d,e,idx+1)
        except:
            return 0
        return tmp

    dic={}
    for i in info:
        a,b,c,d,e=i.split()
        if a in dic:
            if b in dic[a]:
                if c in dic[a][b]:
                    if d in dic[a][b][c]:
                        dic[a][b][c][d][1].append(int(e))
                    else:
                        dic[a][b][c][d]=[0,[int(e)]]
                else:
                    dic[a][b][c]={d:[0,[int(e)]]}
            else:
                dic[a][b]={c:{d:[0,[int(e)]]}}
        else:
            dic[a]={b:{c:{d:[0,[int(e)]]}}}

    for i in query:
        tmp=i.replace('and','')
        a,b,c,d,e=tmp.split()
        e=int(e)
        r=func(a,b,c,d,e,0)
        answer.append(r)
    return answer