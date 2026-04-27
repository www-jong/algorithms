def solution(my_str, n):
    answer=[]
    cnt=0
    tmp=''
    for i in range(len(my_str)):
        if cnt!=n:
            tmp+=my_str[i]
            cnt+=1
        else:
            answer.append(tmp)
            tmp=my_str[i]
            cnt=1
    answer.append(tmp)
    return answer