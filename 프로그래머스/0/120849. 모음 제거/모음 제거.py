def solution(my_string):
    answer = ''
    d={'a','e','i','o','u'}
    for i in my_string:
        if i not in d:
            answer+=i
    return answer