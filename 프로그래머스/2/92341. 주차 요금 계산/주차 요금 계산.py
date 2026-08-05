import math
def solution(fees, records):
    answer = []
    d={}
    def conv(time):
        hour,minute=time.split(":")
        return int(hour)*60+int(minute)

    def calc(time):
        if time<=fees[0]:
            return 0
        time-=fees[0]
        return math.ceil(time/fees[2])*fees[3]
    
    for i in records:
        time,num,flag=i.split()
        if num in d:
            if flag=='IN':
                d[num][1]=conv(time)
                d[num][2]=1
            else:
                now=conv(time)-d[num][1]
                d[num][0]+=conv(time)-d[num][1]
                d[num][2]=0
        else:
            d[num]=[0,conv(time),1]

    for k,v in d.items():
        if v[2]==1:
            v[0]+=conv('23:59')-v[1]
            v[2]=0
        tmp=fees[1]+calc(v[0])
        answer.append((k,tmp))

    answer.sort(key=lambda x:x[0])
    return [b for a,b in answer]