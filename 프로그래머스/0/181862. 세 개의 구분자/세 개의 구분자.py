def solution(myStr):
    myStr=myStr.replace('a',' ').replace('b',' ').replace('c',' ')
    answer = myStr.split()
    return answer if answer else ['EMPTY']