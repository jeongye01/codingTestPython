#https://school.programmers.co.kr/learn/courses/30/lessons/1844
#내 풀이->테스트 통과 DATE=>6.14 풀이시간 15분 
from collections import deque

def solution(maps):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    q = deque([(0, 0)])
    m, n = len(maps[0]), len(maps)
    while q:
        xx, yy = q.popleft()
        for d in range(4):
            nx, ny = xx + dx[d], yy + dy[d]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] += maps[yy][xx]
                q.append((nx, ny))
    return maps[-1][-1] if maps[-1][-1]>1 else -1