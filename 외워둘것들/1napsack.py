#0/1 Knapsack
#내 풀이->테스트 통과 DATE=>5.10 풀이시간 240분 
T = int(input())
for tc in range(1, T + 1):
  n,k=map(int,input().split())
  array=[]
  ans=0
  vt=0
  c=[0]
  v=[0]
  for i in range(n):
    vv,cc=map(int,input().split())
    c.append(cc)
    v.append(vv)
  dp=[[0]*(k+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,k+1):
      if(v[i]>j):
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-v[i]]+c[i])
  ans=dp[n][k]

  print(f"#{tc} {ans}")