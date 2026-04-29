def solution(emergency):
    answer = [0]*len(emergency)
    tmp=[]
    for i in range(len(emergency)):
        tmp.append((emergency[i],i))
    tmp.sort(key=lambda x:-x[0])
    for i in range(len(emergency)):
        answer[tmp[i][1]]=i+1
    return answer