from itertools import permutations
def solution(spell, dic):
    d=set()
    for i in permutations(spell,len(spell)):
        d.add(''.join(i))
    for i in dic:
        if i in d:
            return 1
    return 2