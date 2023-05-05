#재미있는 오셀로 게임
#내 풀이->테스트 통과 DATE=>5.5 풀이시간 120분 
T = int(input())
dx=[0,-1,0,1,-1,-1,1,1]
dy=[-1,0,1,0,-1,1,-1,1]

def check(x,y,p):
  global n,board
  result=[]
  np=1 if p==2 else 2
  for d in range(8):
    i=1
    found=False
    nxp,nyp=x+dx[d],y+dy[d]
    while 0<=nxp<n and 0<=nyp<n:
      if(board[nyp][nxp]==p):
        found=True
        break  
      i+=1
      nxp+=dx[d]
      nyp+=dy[d]
    if(not found):
      i=1
    tmp=[]
    for k in range(1,i):
      nxnp,nynp=x+dx[d]*k,y+dy[d]*k
      
      if(0<=nxnp<n and 0<=nynp<n):
        if(board[nynp][nxnp]==np):
          tmp.append((nxnp,nynp))
        else:
          tmp=[]
          break
    if(len(tmp)>0):
      result+=tmp
  return result
      

for tc in range(1, T + 1):
  n,m=map(int,input().split()) #n->4,8,6 중 m->플레이어가 돌을 놓는 횟수
  seq=[list(map(int,input().split())) for _ in range(m)]
  board=[[0]*n for _ in range(n)]

  # 돌의 색이 1이면 흑돌, 2이면 백돌이다.
  bc,wc=0,0
  
  board[n//2-1][n//2-1]=2
  board[n//2-1][n//2]=1
  board[n//2][n//2-1]=1
  board[n//2][n//2]=2

  for s in seq:
    x,y,p=s
    if(board[y-1][x-1]==0): #빈칸인 경우
      check_result=check(x-1,y-1,p)
      if(len(check_result)>0):
        board[y-1][x-1]=p
        for c in check_result:
          nxnp,nynp=c
          board[nynp][nxnp]=p
  for i in range(n):
    for j in range(n):
      if(board[i][j]==1):
        bc+=1
      elif(board[i][j]==2):
        wc+=1
  
  print("#{} {} {}".format(tc,bc,wc))