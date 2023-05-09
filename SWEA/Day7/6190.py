#정곤이의 단조 증가하는 수
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 30분 
from itertools import combinations
T = int(input())
def check(tmp):
  for x in range(1,len(tmp)):
    if int(tmp[x])<int(tmp[x-1]):
      return False
  return True
    
for tc in range(1,T+1):
  n=int(input())
  array=list(map(int,input().split()))
      
  ans=0
  combs=list(combinations(array,2))
  for comb in combs:
      tmp=comb[0]*comb[1]
      if(check(str(tmp))):
         ans=max(ans,tmp)
  ans=-1 if ans==0 else ans
  print(f"#{tc}",ans)