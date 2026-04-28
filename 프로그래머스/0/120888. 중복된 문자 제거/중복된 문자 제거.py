def solution(my_string):
    answer = ''
    d={}
    for i in my_string:
        if i not in d:
            d[i]=1
            answer+=i
    return answer