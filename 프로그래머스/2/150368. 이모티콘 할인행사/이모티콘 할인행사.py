from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    emo_val=[[i*j//100 for j in range(90,50,-10)] for i in emoticons]

    for i in product([0,1,2,3],repeat=len(emoticons)):
        tmp=[0,0]
        for x,y in users:
            now=0
            for j in range(len(emoticons)):
                if (i[j]+1)*10>=x:
                    now+=emo_val[j][i[j]]
            if now<y:
                tmp[1]+=now
            else:
                tmp[0]+=1

        if tmp[0]>answer[0] or tmp[0]==answer[0] and tmp[1]>answer[1]:
            answer=tmp
    return answer