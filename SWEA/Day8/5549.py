#홀수일까 짝수일까
#내 풀이->테스트 통과 DATE=>5.10 풀이시간 2분 
T = int(input())
for tc in range(1, T + 1):
  n=int(input())
  ans="Odd"
  if(n%2==0):
    ans="Even"
  print(f"#{tc} {ans}")