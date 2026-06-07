def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col-1],-x[0]))
    idx=row_begin
    for i in data[row_begin-1:row_end]:
        tmp=0
        for j in i:
            tmp+=j%idx
        answer^=tmp
        idx+=1
    return answer