def solution(msg):
    dic={chr(i+65):i+1 for i in range(26)}
    answer = []
    count=27
    i=0
    while i<len(msg):
        idx=1
        c=1
        check=0
        tmp_word=''
        while i+idx<=len(msg):
            if msg[i:i+idx] in dic:
                tmp_word=msg[i:i+idx]
                check=1
                idx+=1
            else:
                check=1
                dic[msg[i:i+idx]]=count
                break
        answer.append(dic[tmp_word if tmp_word else msg[i:i+idx]])
        count+=1
        i+=idx-1
    return answer