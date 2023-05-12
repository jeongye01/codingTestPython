# 연구소
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트
for _ in range(n):
    data.append(list(map(int, input().split())))


# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

result = 0


# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우 
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2 
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(result)



'''
#내풀이 -> 테스트 통과  DATE->4.17 풀이시간->60분
from itertools import combinations
import copy
n,m=map(int,input().split())
array=[]
comb=[]
for y in range(n):
  data=list(map(int,input().split()))
  array.append(data)
  for x in range(m):
    if(data[x]==0):
      comb.append((x,y))


graph=[]

def dfs(x,y):
  if(x<0 or x>=m or y<0 or y>=n):
    return
  if(graph[y][x]!=0):
    return
  graph[y][x]=2
  dfs(x-1,y)
  dfs(x,y-1)
  dfs(x+1,y)
  dfs(x,y+1)
  



result=0
for walls in list(combinations(comb, 3)):
  graph=copy.deepcopy(array)
  for wall in walls:
    x,y=wall
    graph[y][x]=1
  for i in range(n):
    for j in range(m):
      if(graph[i][j]==2):
         dfs(j-1,i)
         dfs(j,i-1)
         dfs(j+1,i)
         dfs(j,i+1)
  safe=0
  for i in range(n):
    for j in range(m):
      if(graph[i][j]==0):
        safe+=1
  result=max(result,safe)
 

print(result)


'''

#2번째 풀이
##내풀이 -> 테스트 통과  DATE->5.12 풀이시간->30분
'''
from itertools import combinations
from collections import deque
import copy
dx=[0,-1,0,1]
dy=[-1,0,1,0]
def bfs(x,y):
  global board2
  q=deque([(x,y)])
  while q:
    now=q.popleft()
    for d in range(4):
      nx,ny=now[0]+dx[d],now[1]+dy[d]
      if 0<=nx<m and 0<=ny<n:
        if board2[ny][nx]==0:
          q.append((nx,ny))
          board2[ny][nx]=2
        
        
  
n,m=map(int,input().split())
board=[]
for _ in range(n):
  board.append(list(map(int,input().split())))
idxs=[]
for i in range(n):
  for j in range(m):
    if(board[i][j]==0):
      idxs.append((i,j))
comb=list(combinations(idxs,3))
ans=0
for c in comb:
  board2=copy.deepcopy(board)
  for pos in c:
    i,j=pos
    board2[i][j]=1
  for i in range(n):
    for j in range(m):
      if board2[i][j]==2:
        bfs(j,i)
  tmp=0
  
  for i in range(n):
    for j in range(m):
      if board2[i][j]==0:
        tmp+=1
  ans=max(ans,tmp)
print(ans)
        



'''