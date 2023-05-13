#https://www.acmicpc.net/problem/1697
#내 풀이->테스트 통과 DATE=>5.13 풀이시간 60분 
from collections import deque
n,k=map(int,input().split())
def bfs():
  q=deque([(n,0)])
  visited[n]=1
  while q:
    p,s=q.popleft()
    if p==k:
      return s
    for np in [2*p,p+1,p-1]:
      if 0<=np<=100000 and visited[np]==0:
        visited[np]=1
        q.append((np,s+1))
    



visited = [0 for i in range(100001)]

print(bfs())