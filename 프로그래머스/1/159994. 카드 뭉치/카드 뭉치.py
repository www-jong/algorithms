def solution(cards1, cards2, goal):
    answer = ''
    cards1=cards1[::-1]
    cards2=cards2[::-1]
    for i in goal:
        if cards1 and i==cards1[-1]:
            cards1.pop()
        elif cards2 and i==cards2[-1]:
            cards2.pop()
        else:
            return 'No'
    
    return 'Yes'