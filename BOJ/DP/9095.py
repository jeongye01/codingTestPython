#1, 2, 3 더하기
#https://jyami.tistory.com/15
#https://www.acmicpc.net/problem/9095
#내 풀이->테스트 통과 DATE=>5.11 풀이시간 60분 
T=int(input())
for tc in range(1,T+1):
  n=int(input())
  dp=[0]*11
  dp[1]=1
  dp[2]=2
  dp[3]=4
  for i in range(4,n+1):
    for j in range(1,4):
      dp[i]+=dp[i-j]
    
  print(dp[n])