#최대수 구하기
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 2분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  array=list(map(int,input().split()))
  ans=max(array)
    
  print("#{} {}".format(test_case,ans))