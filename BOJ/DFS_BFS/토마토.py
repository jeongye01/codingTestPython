#https://www.acmicpc.net/problem/7576
from collections import deque

dx=[0,-1,0,1]
dy=[-1,0,1,0]
def bfs():
    global q,ans,board

    while q:
        x,y,days=q.popleft()
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<m and 0<=ny<n and board[ny][nx]==0:
                q.append((nx,ny,days+1))
                board[ny][nx]=1
                ans=days+1
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                ans=-1
                return



m,n=map(int,input().split())
board=[]
q=deque()
for i in range(n):
    data=list(map(int,input().split()))
    board.append(data)
    for j in range(m):
        if data[j]==1:
            q.append((j,i,0))
ans=0
bfs()
print(ans)