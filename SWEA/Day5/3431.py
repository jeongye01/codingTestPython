#준환이의 운동관리
##내 풀이->테스트 통과 DATE=>5.6 풀이시간 2분 
T = int(input())

for tc in range(1, T + 1):
  l,u,x=map(int,input().split())
  if x>u:
    ans=-1
  elif x<l:
    ans=l-x
  else:
    ans=0
    

  print(f"#{tc} {ans}")