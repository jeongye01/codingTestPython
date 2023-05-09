#다솔이의 월급 상자
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 5분 
T = int(input())
for tc in range(1,T+1):
  n=int(input())
  ans=0
  for _ in range(n):
    p,x=map(float,input().split())
    ans+=p*x
  print(f"#{tc}",format(ans,".6f"))