#https://school.programmers.co.kr/learn/courses/30/lessons/42885
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 5분 
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q=deque(people)
    while q:
        now=q.popleft()
        if q and q[-1]<=limit-now:
            q.pop()
        answer+=1
    return answer