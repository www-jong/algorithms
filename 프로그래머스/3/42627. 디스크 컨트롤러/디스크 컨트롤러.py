import heapq
def solution(jobs):
    answer = 0
    N=len(jobs)
    q1=[(jobs[i][1],jobs[i][0],i)  for i in range(N)]
    q1.sort(key=lambda x:-x[1])
    q2=[]

    li=[]
    time=0
    # 소요시간,요청시각,작업번호
    while q1 or q2:
        while q1:
            if q1[-1][1]<=time:
                a,b,c=q1.pop()
                heapq.heappush(q2,(a,b,c))
            else:
                break
        if q2:
            a,b,c=heapq.heappop(q2)
            time+=a
            answer+=time-b
        elif q1:
            time=q1[-1][1]
    return answer//N if answer else 0