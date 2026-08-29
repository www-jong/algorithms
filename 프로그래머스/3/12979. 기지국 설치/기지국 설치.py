import math
def solution(n, stations, w):
    answer = 0
    li=[]
    for i in range(1,len(stations)):
        li.append(stations[i]-stations[i-1]-w*2-1)
    li.append(stations[0]-w-1)
    li.append(n-stations[-1]-w)
    print(li)

    for i in li:
        if i<=0:
            continue
        else:
            answer+=math.ceil(i/((w*2)+1))
    return answer