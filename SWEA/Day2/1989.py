#초심자의 회문 검사
#내 풀이->테스트 통과 DATE=>5.1 풀이시간 2분 
T = int(input())

for test_case in range(1, T + 1):
  s=input()
  ans=0
  if(s==s[::-1]):
    ans=1
  
  
  print("#{} {}".format(test_case,ans))


