# 쥬스 나누기
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 5분 
T = int(input())
for tc in range(1,T+1):
  n=int(input())
  result=[f"1/{n}" for i in range(1,n+1)]
  print(f"#{tc}",*result)