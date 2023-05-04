#[S/W 문제해결 기본] 3일차 - 회문2
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 40분 
dx=[0,1]
dy=[1,0]

def dfs(x,y,s,d):
  global board,ans
  #print(x,y,size,ans)
  if(x<0 or x>=size or y<0 or y>=size):
    return 
  news=s+board[y][x]
  if(news==news[::-1]):
    ans=news if len(ans)<len(news) else ans
  nx,ny=x+dx[d],y+dy[d]
  dfs(nx,ny,news,d)
  

T = 10
for test_case in range(1, T + 1):
  n=int(input())
  size=100
  board=[list(input()) for _ in range(size)]
  ans=""
  for i in range(size):
    for j in range(size):
      for d in range(2):
        dfs(j,i,"",d)
  print("#{} {}".format(test_case,len(ans)))

