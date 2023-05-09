#직사각형 길이 찾기
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 5분 
T = int(input())
for tc in range(1,T+1):
  array=list(map(int,input().split()))
  s1,s2=array[0],array[1]
  if(s1==s2):
    ans=array[2]
  elif(array[2]==s1):
    ans=array[1]
  else:
    ans=array[0]
  print(f"#{tc}",ans)