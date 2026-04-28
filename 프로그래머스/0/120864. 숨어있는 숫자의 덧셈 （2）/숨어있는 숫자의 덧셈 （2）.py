def solution(my_string):
    tmp=''
    for i in my_string:
        if i.isalpha():
            tmp+=' '
        else:
            tmp+=i
    answer=sum([int(i) for i in tmp.split()])
    return answer