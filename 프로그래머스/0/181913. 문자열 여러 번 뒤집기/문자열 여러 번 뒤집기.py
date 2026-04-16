def solution(my_string, queries):
    answer = list(my_string)

    for s,e in queries:
        tmp=[i for i in answer]
        tmp[s:e+1]=tmp[s:e+1][::-1]
        answer=tmp
    return ''.join(answer)