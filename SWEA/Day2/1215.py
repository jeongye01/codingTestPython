# [S/W 문제해결 기본] 3일차 - 회문1
#내 풀이->테스트 통과 DATE=>5.30 풀이시간 45분 
T = 10

dx=[0,1]
dy=[1,0]
board=[]
size=8
def dfs(n,s,x,y,d):
  global board,size
  if(x<0 or x>=size or y<0 or y>=size):
    return 0
  news=s+board[y][x]
  nx,ny=x+dx[d],y+dy[d]
  if(news==news[::-1] and len(news)==n):
    return 1
  else:
    return dfs(n,news,nx,ny,d)
  
def find(n):
  global board,size
  result=0
  for i in range(size):
    for j in range(size):
      for d in range(2):
        result+=dfs(n,"",j,i,d)
        
  return result
  
  
for test_case in range(1, T + 1):
  n=int(input())
  board=[]
  for _ in range(size):
    board.append(list(input())) 
  ans=find(n)
  print("#{}".format(test_case),ans)


