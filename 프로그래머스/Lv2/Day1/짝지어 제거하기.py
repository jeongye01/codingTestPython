#https://school.programmers.co.kr/learn/courses/30/lessons/12973/solution_groups?language=python3&type=my
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 10분 
from collections import deque
def solution(s):
    q=deque()
    for x in s:
        if q and q[-1]==x:
            q.pop()
        else:
            q.append(x)

    return 0 if q else 1