#24시간
#내 풀이->테스트 통과 DATE=>5.10 풀이시간 3분 
T = int(input())
for tc in range(1, T + 1):
  a,b=map(int,input().split())
  ans=(a+b)%24
  print(f"#{tc} {ans}")