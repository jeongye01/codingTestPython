#1차원 정원
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 5분 
import math
T = int(input())
for tc in range(1,T+1):
  n,d=map(int,input().split())
  ans=math.ceil(n/(d*2+1))
  print(f"#{tc}",ans)