#https://school.programmers.co.kr/learn/courses/30/lessons/42586
##내 풀이->테스트 통과 DATE=>6.5 풀이시간 15분 
from collections import deque
def solution(progresses, speeds):
    pq = deque(progresses)
    sq = deque(speeds)
    answer = []
    d=0
    while pq:
        p = pq.popleft()
        s = sq.popleft()
        if d>=(100 - p - 1) // s + 1:
            answer[-1]+=1
        else:
            d = (100 - p - 1) // s + 1
            answer.append(1)

    return answer