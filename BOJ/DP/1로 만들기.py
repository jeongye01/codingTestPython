##내 풀이->테스트 통과 DATE=>5.22 풀이시간 15분 
#https://www.acmicpc.net/problem/1463
n=int(input())
dp=[0]*(n+1)

for i in range(2,n+1):
  dp[i]=dp[i-1]+1
  if i%2==0:
    dp[i]=min(dp[i],dp[i//2]+1)
  if i%3==0:
    dp[i]=min(dp[i],dp[i//3]+1)
print(dp[n])