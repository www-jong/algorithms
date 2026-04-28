def solution(id_pw, db):
    answer = ''
    d={}
    for i,j in db:
        d[i]=j
    if id_pw[0] in d:
        if d[id_pw[0]]==id_pw[1]:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail'