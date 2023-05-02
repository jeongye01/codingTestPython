# [S/W 문제해결 기본] 3일차 - String
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  n=int(input())  
  s=input()
  p=input()
  print(f"#{test_case}", p.count(s)) 