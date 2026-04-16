def solution(code):
    answer = ''
    mode=0
    for i in range(len(code)):
        if mode:
            if code[i]=='1':
                mode^=1
            elif i%2:
                answer+=code[i]
        else:
            if code[i]=='1':
                mode^=1
            elif i%2==0:
                answer+=code[i]
                
    return answer if answer else "EMPTY"