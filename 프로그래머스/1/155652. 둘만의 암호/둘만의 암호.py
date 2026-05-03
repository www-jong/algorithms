def solution(s, skip, index):
    answer = '' #122
    d=[chr(i) for i in range(97,123) if chr(i) not in skip]
    print(d)
    for i in s:
        tar=(d.index(i)+index)%len(d)
        answer+=d[tar]
    return answer