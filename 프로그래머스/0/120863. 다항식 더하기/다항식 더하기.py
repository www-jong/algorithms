def solution(polynomial):
    answer = ''
    x=0
    y=0
    for i in polynomial.split():
        if i[-1]=='x':
            #print(i)
            if len(i)>=2:
                #print(i[:-1])
                x+=int(i[:-1])
            else:
                x+=1
        elif i[0]=='+':
            continue
        else:
            y+=int(i)
    #print(x,y)
    if x and y:
        return f'{x if x!=1 else ""}x + {y}'
    elif x:
        return f'{x if x!=1 else ""}x'
    else:
        return str(y)