from collections import deque
def solution(plans):
    answer = []
    for i in range(len(plans)):
        h,m=plans[i][1].split(":")
        t=int(h)*60+int(m)
        plans[i][1]=t
        plans[i][2]=int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    q1=deque(plans)
    q2=deque()
    now_name,now_st,now_play=q1.popleft()
    time=now_st
    while q1:
        next_name,next_st,next_play=q1.popleft()
        if time+now_play<=next_st:
            answer.append(now_name)
            time+=now_play
            while q2 and time<next_st:
                tmp_name,tmp_play=q2.pop()
                if time+tmp_play<=next_st:
                    answer.append(tmp_name)
                    time+=tmp_play
                else:
                    tmp_play-=next_st-time
                    q2.append([tmp_name,tmp_play])
                    break
            now_name,now_st,now_play=next_name,next_st,next_play
            time=now_st
        else:
            now_play-=next_st-time
            q2.append([now_name,now_play])
            now_name,now_st,now_play=next_name,next_st,next_play
            time=now_st
    answer.append(now_name)
    while q2:
        answer.append(q2.pop()[0])
    return answer