#격자판 칠하기
#내 풀이->테스트 통과 DATE=>5.14 풀이시간 35분 
from collections import deque
dx=[0,-1,0,1]
dy=[-1,0,1,0]


def check():
    for i in range(n):
        for j in range(m):
            for d in range(4):
                nx, ny = j + dx[d], i + dy[d]
                if 0 <= nx < m and 0 <= ny < n:
                    if board[ny][nx]==board[i][j]:
                        return False
    return True


def bfs(x,y):
    global visited,board,ans
    # '#'은 검은색 '.'은 흰색
    q=deque([(x,y)])
    visited[y][x]=True

    while q:
        (xx,yy)=q.popleft()
        for d in range(4):
            nx,ny=xx+dx[d],yy+dy[d]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
                if board[ny][nx]=="?":
                    if board[yy][xx] == "#":
                        board[ny][nx] = '.'
                    elif board[yy][xx] == ".":
                        board[ny][nx] = '#'
                visited[ny][nx]=True
                q.append((nx,ny))






T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    board=[]
    for _ in range(n):
        board.append(list(input()))
    visited=[[False]*m for _ in range(n)]
    ans='impossible'
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j]!='?':
                bfs(j,i)
                flag=True
                break
        if flag:
            break

    if flag==False or check():
        ans="possible"


    print(f"#{tc} {ans}")