#[S/W 문제해결 기본] 10일차 - 비밀번호
##내 풀이->테스트 통과 DATE=>5.5 풀이시간 15분 
T = 10
for tc in range(1, T + 1):
  n,s=input().split()
  n=int(n)
  s=list(s)
  i=0
  while i+1<len(s):
    if(s[i]==s[i+1]):
      del s[i]
      del s[i]
      i-=1
    else:
      i+=1
  ans="".join(s)
  print("#{} {}".format(tc,ans))