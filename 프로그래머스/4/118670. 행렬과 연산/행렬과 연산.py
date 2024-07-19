from collections import deque
def solution(rc, operations):
    rotate_left=deque()
    rotate_right=deque()
    center_pair=deque()
    for x in range(len(rc)):
        rotate_left.append(rc[x][0])
        rotate_right.append(rc[x][-1])
        center_pair.append(deque((rc[x][1:-1])))

    def shiftrow():
        rotate_left.appendleft(rotate_left.pop())
        rotate_right.appendleft(rotate_right.pop())
        center_pair.appendleft(center_pair.pop())

    def rotate():
        if len(rc[0])>2:
            rotate_right.appendleft(center_pair[0].pop())
            center_pair[-1].append(rotate_right.pop())
            rotate_left.append(center_pair[-1].popleft())
            center_pair[0].appendleft(rotate_left.popleft())
        else:
            rotate_right.appendleft(rotate_left.popleft())
            rotate_left.append(rotate_right.pop())
    for operation in operations:
        if operation=="ShiftRow":
            shiftrow()
            pass
        else:
            rotate()
    answer = []
    for x in range(len(rc)):
        tmp=[rotate_left.popleft()]+list(center_pair.popleft())+[rotate_right.popleft()]
        answer.append(tmp)
    return answer

