def solution(dot):
    x,y=dot
    if x>0:
        return 1 if y>0 else 4
    else:
        return 2 if y>0 else 3