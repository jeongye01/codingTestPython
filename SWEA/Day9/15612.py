#체스판 위의 룩 배치
#내 풀이->테스트 통과 DATE=>5.17 풀이시간 20분 
dx=[0,-1,0,1]
dy=[-1,0,1,0]
n=8
def dfs(x,y,d):
  if x<0 or x>=n or y<0 or y>=n:
    return True
  if board[y][x]=="O":
    return False
  nx,ny=x+dx[d],y+dy[d]
  return dfs(nx,ny,d)
    
  

T=int(input())
for tc in range(1,T+1):
  ans="yes"
  #n=int(input())
  board=[]
  for _ in range(8):
    board.append(list(input()))
  cnt=0
  for i in range(8):
    for j in range(8):
      if board[i][j]=='O':
        cnt+=1
        for d in range(4):
          nx,ny=j+dx[d],i+dy[d]
          if(dfs(nx,ny,d)==False):
            ans="no"
            break
  if cnt!=8:
    ans="no"
  
  
  print(f'#{tc} {ans}')