def rev(a):
    tmp=[max(a),min(a)]
    return tmp

def solution(wallet, bill):
    wallet=rev(wallet)
    bill=rev(bill)
    answer = 0
    while wallet[0]<bill[0] or wallet[1]<bill[1]:
        bill[0]//=2
        bill=rev(bill)
        answer+=1
    return answer