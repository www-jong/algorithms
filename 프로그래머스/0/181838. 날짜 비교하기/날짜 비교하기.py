def func(date):
    return str(date[0]).zfill(5)+str(date[1]).zfill(2)+str(date[2]).zfill(2)
def solution(date1, date2):
    if int(func(date1))<int(func(date2)):
        return 1
    else:
        return 0