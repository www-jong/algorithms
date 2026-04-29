def solution(age):
    d='abcdefghij'
    answer = ''
    for i in str(age):
        answer+=d[int(i)]
    return answer