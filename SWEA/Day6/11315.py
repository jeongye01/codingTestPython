# 오목 판정
#내 풀이->테스트 통과 DATE=>5.8 풀이시간 12분 
T = int(input())
dx=[0,-1,0,1,1,1,-1,-1]
dy=[-1,0,1,0,-1,1,-1,1]

def check(x,y,d,m):
  global ans
  nx,ny=x+dx[d],y+dy[d]
  if m==5:
    ans="YES"
    return
  if(0<=nx<n and 0<=ny<n):
    if(0<=nx<n and 0<=ny<n):
      if board[ny][nx]=="o":
        check(nx,ny,d,m+1)
  

def sol():
  global ans
  for i in range(n):
    for j in range(n):
      if(board[i][j]=="o"):
        for d in range(8):
          check(j,i,d,1)
        if(ans=="YES"):
          return
for tc in range(1,T+1):
  ans="NO"
  board=[]
  n=int(input())
  for _ in range(n):
    board.append(list(input()))
  
  sol()
  print(f"#{tc}",ans)