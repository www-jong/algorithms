import heapq
def solution(operations):
    answer = []
    minh=[]
    maxh=[]
    visit=[0]*(len(operations))
    lenh=0
    for i,op in enumerate(operations):
        oper,num=op.split()
        num=int(num)
        visit[i]=1
        if oper=='I':
            heapq.heappush(minh,(num,i))
            heapq.heappush(maxh,(-num,i))
        else:
            if num==1:
                while maxh and not visit[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    visit[maxh[0][1]]=0
                    heapq.heappop(maxh)
            else:
                while minh and not visit[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    visit[minh[0][1]]=0
                    heapq.heappop(minh)
    while maxh and not visit[maxh[0][1]]:
        heapq.heappop(maxh)
    while minh and not visit[minh[0][1]]:
        heapq.heappop(minh)
    
    if not minh:
        return [0,0]
    return [-maxh[0][0],minh[0][0]]
