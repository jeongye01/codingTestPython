#최장 증가 부분 수열
#내 풀이->테스트 통과 DATE=>5.8 풀이시간 100분 
T = int(input())
for tc in range(1,T+1):
  dp=[0]*1000
  n=int(input())
  array=list(map(int,input().split()))
  ans=0
  for k in range(n):
    dp[k]=1
    for i in range(k):
      if(array[i] < array[k]):
        dp[k] = max(dp[k], dp[i] + 1)
      
    

  ans=max(dp)   
  #print(dp)
  
  print(f"#{tc}",ans)