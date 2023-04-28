#[S/W 문제해결 기본] 2일차 - Sum
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 17분 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  n=int(input())
  board=[]
  ans=0
  size=100
  for _ in range(size):
    board.append(list(map(int,input().split())))
  result=[]
  a1s=0
  a2s=0
  for i in range(size):
    cs=0
    rs=0
    for j in range(size):
      cs+=board[i][j]
      rs+=board[j][i]
      if(i==j):
        a1s+=board[i][j]
      if(i==size-1-j):
        a2s+=board[i][j]
        
    result.append(cs)
    result.append(rs)
  result.append(a1s)
  result.append(a2s)

  ans=max(result)
    
  print("#{} {}".format(test_case,ans))