#숫자 조작
#내 풀이->테스트 통과 DATE=>5.11 풀이시간 50분 
from itertools import combinations
T=int(input())
for tc in range(1,T+1):
  nInput=input()
  n=list(nInput)
  if int(nInput)<=10:
    print(f"#{tc}",nInput,nInput)
    continue

    
  idxs=[i for i in range(len(n))]
  comb=list(combinations(idxs,2))
  max_ans=0
  min_ans=1e9
  toint=int("".join(n))
  max_ans=max(max_ans,toint)
  min_ans=min(min_ans,toint)
  for c in comb:
    idx1,idx2=c
    n[idx1],n[idx2]=n[idx2],n[idx1]
    if n[0]!="0":
      toint=int("".join(n))
      max_ans=max(max_ans,toint)
      min_ans=min(min_ans,toint)
    n[idx1],n[idx2]=n[idx2],n[idx1]
      
  

  print(f"#{tc}",min_ans,max_ans)