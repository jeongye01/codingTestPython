#https://school.programmers.co.kr/learn/courses/30/lessons/12927
##내 풀이->테스트 통과 DATE=>6.27 풀이시간 10분 
import heapq
def solution(n, works):
    answer=0
    q=[]
    for w in works:
        heapq.heappush(q,w*-1)
    while q and n:
        now=heapq.heappop(q)
        now+=1
        n-=1
        if now!=0:
            heapq.heappush(q,now)
    while q:
        now = heapq.heappop(q)
        answer+=now**2
    return answer