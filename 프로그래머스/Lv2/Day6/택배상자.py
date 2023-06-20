#https://school.programmers.co.kr/learn/courses/30/lessons/131704
##내 풀이->테스트 통과 DATE=>6.20 풀이시간 20분 
from collections import deque
def solution(order):
    answer = 0
    q=deque()
    order=deque(order)
    for number in range(1,len(order)+2):
        if number==order[0]:
            answer += 1
            order.popleft()
        else:
            while order and q and order[0]==q[0]:
                answer+=1
                order.popleft()
                q.popleft()
            q.appendleft(number)

    return answer