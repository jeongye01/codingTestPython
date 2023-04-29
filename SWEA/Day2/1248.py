#수도 요금 경쟁
#내 풀이->테스트 통과 DATE=>4.29 풀이시간 10분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  p,q,r,s,w=map(int,input().split())
  ans=0
  if(w<=r):
    ans=min(p*w,q)
  else:
    ans=min(p*w,q+s*(w-r))

  print("#{} {}".format(test_case,ans))