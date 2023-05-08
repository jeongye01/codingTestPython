#의석이의 세로로 말해요
#내 풀이->테스트 통과 DATE=>5.8 풀이시간 8분 
T = int(input())
for tc in range(1,T+1):
  board=[]
  ans=""
  maxlength=0
  for _ in range(5):
    tmp=list(input())
    board.append(tmp)
    maxlength=max(maxlength,len(tmp))

  for i in range(maxlength):
    for j in range(5):
      if(i<len(board[j])):
        ans+=board[j][i]
  print(f"#{tc}",ans)