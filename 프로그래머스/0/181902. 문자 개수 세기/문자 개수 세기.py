def solution(my_string):
    answer = [0]*52
    for i in range(ord('A'),ord('A')+26):
        answer[i-ord('A')]=my_string.count(chr(i))
    for i in range(ord('a'),ord('a')+26):
        answer[26+i-ord('a')]=my_string.count(chr(i))
    return answer