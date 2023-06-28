#https://school.programmers.co.kr/learn/courses/30/lessons/12987
##내 풀이->테스트 통과 DATE=>6.28 풀이시간 20분 
from collections import deque
def solution(A, B):
    aq=deque(sorted(A))
    bq=deque(sorted(B))
    answer = 0
    while bq:
        while bq and aq[0]>=bq[0]:
            bq.popleft()
        if bq:
            aq.popleft()
            bq.popleft()
            answer += 1


    return answer