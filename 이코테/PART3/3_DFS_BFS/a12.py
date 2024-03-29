from collections import deque
n, k = map(int, input().split())
graph = [] # 전체 보드 정보를 담는 리스트 
data = [] # 바이러스에 대한 정보를 담는 리스트
for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))
# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])


'''
#내풀이 -> 테스트 통과  DATE->4.17 풀이시간->180분
from collections import deque

n,k=map(int,input().split())

graph=[]
start=[[] for _ in range(k+1)]
for _y in range(n):
    data=list(map(int,input().split()))
    graph.append(data)
    for _x in range(n):
        if(data[_x]!=0):
            start[data[_x]].append((_x,_y))

s,ix,iy=map(int,input().split())

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(t,v):
    global graph
    q=deque(start[v])
    #print(q)
    newQ=deque()
    while q:
        (x,y)=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(nx>=0 and nx<n and ny>=0 and ny<n):
                if(graph[ny][nx]==0):
                    graph[ny][nx]=v
                    newQ.append((nx,ny))
    start[v]=list(newQ)
    
       
for t in range(1,s+1):
    for v in range(1,k+1):
        bfs(t,v)

print(graph[ix-1][iy-1])



'''
#내풀이 -> 테스트 통과  DATE->5.12 풀이시간->30분
'''

from collections import deque
dx=[0,-1,0,1]
dy=[-1,0,1,0]
def bfs():
  global visited,board
  q=deque()
  for v in virus:
    q.append(v) # x,y
    visited[v[2]][v[1]]=True
  timer=0
  tmp=0
  while q:
    now=q.popleft()
    if tmp>now[0]:
      timer+=1
    tmp=now[0]
    if timer>=s:
      return 
    for d in range(4):
      nx,ny=now[1]+dx[d],now[2]+dy[d]
      if 0<=nx<n and 0<=ny<n:
        if visited[ny][nx]==False and board[ny][nx]==0 :
          q.append((now[0],nx,ny))
          visited[ny][nx]=True
          board[ny][nx]=now[0]
        
        
  
n,k=map(int,input().split())
board=[]
virus=[]
for i in range(n):
  data=list(map(int,input().split()))
  board.append(data)
  for j in range(n):
    if data[j]!=0:
      virus.append([data[j],j,i])     
virus.sort(key=lambda x:x[0])
s,x,y=map(int,input().split())
visited=[[False]*n for _ in range(n)]
bfs()

#for b in board:
 # print(*b)
ans=board[x-1][y-1]
print(ans)
        

  
  



'''