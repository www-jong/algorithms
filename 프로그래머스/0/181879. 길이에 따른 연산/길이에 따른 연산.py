def solution(num_list):
    r=1
    for i in num_list:
        r*=i
    answer = sum(num_list) if len(num_list)>=11 else r
    return answer