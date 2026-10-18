def solution(play_time, adv_time, logs):
    answer = 0
    def time_conv(t):
        h,m,s=map(int,t.split(':'))
        return h*3600+m*60+s
    def to_str(t):
        return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"
    play=time_conv(play_time)
    ad=time_conv(adv_time)
    li=[0]*(play+1)
    for i in logs:
        st,end=map(time_conv,i.split('-'))
        li[st]+=1
        li[end]-=1
    for i in range(1,play):
        li[i]+=li[i-1]
    now=sum(li[:ad])
    max_v=now
    
    for i in range(1,play-ad+1):
        now-=li[i-1]
        now+=li[i+ad-1]
        if now>max_v:
            max_v=now
            answer=i
    return to_str(answer)