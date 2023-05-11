#새샘이의 7-3-5 게임
#내 풀이->테스트 통과 DATE=>5.11 풀이시간 6분 
from itertools import combinations
T=int(input())
for tc in range(1,T+1):
  array=list(map(int,input().split()))
  comb=list(combinations(array,3))
  result=set()
  for c in comb:
    result.add(sum(c))
      
  result=list(result)
  result.sort(reverse=True)
  
  print(f"#{tc}",result[4])