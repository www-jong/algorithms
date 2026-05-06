def solution(ingredient):
    answer = 0
    q=[]
    for i in ingredient:
        q.append(i)
        if len(q)>=4:
            if ''.join(map(lambda x:str(x),q[-4:]))=='1231':
                for _ in range(4):q.pop()
                answer+=1
    return answer