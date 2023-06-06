#https://school.programmers.co.kr/learn/courses/30/lessons/42587
#내 풀이->테스트 통과 DATE=>6.5 풀이시간 25분 
from collections import deque
def solution(priorities, location):
    q = deque()
    answer = 0
    for i, p in enumerate(priorities):
        q.append((p,i))
    while q:
        p,i=q.popleft()
        canDo=True
        for e in q:
            if e[0]>p:
                q.append((p,i))
                canDo=False
                break

        if canDo:
            answer += 1
            if i==location:
                return answer
    return answer