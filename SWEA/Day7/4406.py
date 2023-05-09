# 모음이 보이지 않는 사람
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 5분 
T = int(input())
for tc in range(1,T+1):
  mo=["a","e","i","o","u"]
  s=input()
  ans=""
  for i in range(len(s)):
    if s[i] not in mo:
      ans+=s[i]
  print(f"#{tc}",ans)