#https://school.programmers.co.kr/learn/courses/30/lessons/43162
#내 풀이->테스트 통과 DATE=>6.27 풀이시간 17분 
from collections import deque

def solution(n, computers):
    answer = 0
    visited=[False]*n
    for i in range(n):
        if not visited[i]:
            q=deque([i])
            answer+=1
            while q:
                now=q.popleft()
                for j in range(n):
                    if computers[now][j]==1  and not visited[j]:
                        visited[j]=True
                        q.append(j)
    return answer