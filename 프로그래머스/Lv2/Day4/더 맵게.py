#https://school.programmers.co.kr/learn/courses/30/lessons/42626
###내 풀이->테스트 통과 DATE=>6.11 풀이시간 10분 
import heapq
def solution(scoville, K):
    q = []
    answer = 0
    for s in scoville:
        heapq.heappush(q, s)
    while len(q)>=2 and q[0] < K:
        answer += 1
        s1 = heapq.heappop(q)
        s2 = heapq.heappop(q)
        heapq.heappush(q, s1 + s2 * 2)

    return answer if q[0]>=K else -1