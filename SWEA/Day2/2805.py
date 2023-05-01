#농작물 수확하기
#내 풀이->테스트 통과 DATE=>5.1 풀이시간 15분 
T = int(input())

for test_case in range(1, T + 1):
  
  n=int(input())
  board=[]
  ans=0
  for _ in range(n):
    board.append(list(input()))
  #print(board)
  for i in range(n):
    diff=abs(n//2-i)
    #print(diff,diff+n-diff*2)
    for j in range(diff,diff+n-diff*2):
      ans+=int(board[i][j])

  print("#{}".format(test_case),ans)
