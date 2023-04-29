#패턴 마디의 길이
#내 풀이->테스트 통과 DATE=>4.29 풀이시간 25분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  s=input()
  ans=0
  
  for i in range(1,11):
    pattern=s[0:i] 
    isPattern=True
    for j in range(len(pattern),len(s),len(pattern)):
      #print(pattern,s[j:j+len(pattern)])
      if(len(s[j:j+len(pattern)])<len(pattern)):
        break
      if(pattern!=s[j:j+len(pattern)]):
        isPattern=False
        break
    if(isPattern):
      ans=len(pattern)
      break
   
  print("#{} {}".format(test_case,ans))