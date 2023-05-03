
#[S/W 문제해결 기본] 4일차 - 거듭 제곱
#내 풀이->테스트 통과 DATE=>5.2 풀이시간 2분 
T = 10

for test_case in range(1, T + 1):
  n=int(input())
  a,b=map(int,input().split())
  print("#{} {}".format(test_case,pow(a,b)))