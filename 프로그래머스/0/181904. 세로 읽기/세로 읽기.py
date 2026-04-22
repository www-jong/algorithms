def solution(my_string, m, c):
    li=[]
    for i in range(len(my_string)//m):
        li.append(my_string[i*m:(i+1)*m])
    answer = ''.join([i[c-1] for i in li if len(i)>=c])
    return answer