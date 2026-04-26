def solution(order):
    d=set(['iceamericano','americanoice','hotamericano','americanohot','anything','americano'])
    answer = 0
    for i in order:
        if i in d:
            print(i)
            answer+=4500
        else:
            answer+=5000
    return answer