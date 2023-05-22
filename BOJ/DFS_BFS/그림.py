#https://www.acmicpc.net/problem/1926
#내 풀이->테스트 통과 DATE=>5.22 풀이시간 15분 
from collections import deque
cnt=0
big=0

dx=[0,-1,0,1]
dy=[-1,0,1,0]
def bfs(x,y):
  global visited,big
  area=1
  q=deque([(x,y)])
  visited[y][x]=True
  while q:
    xx,yy=q.popleft()
    for d in range(4):
      nx,ny=xx+dx[d],yy+dy[d]
      if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and paint[ny][nx]==1:
        visited[ny][nx]=True
        q.append((nx,ny))
        area+=1
  big=max(big,area)
        
      
    
    
  
  

n,m=map(int,input().split())
paint=[]
for _ in range(n):
  paint.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if paint[i][j]==1 and not visited[i][j]:
      cnt+=1
      bfs(j,i)

print(cnt)
print(big)