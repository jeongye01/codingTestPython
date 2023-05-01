#아주 간단한 계산기
#내 풀이->테스트 통과 DATE=>5.1 풀이시간 2분 
T = 1

for test_case in range(1, T + 1):
  a,b=map(int,input().split())
  
  print(a+b)
  print(a-b)
  print(a*b)
  print(a//b)