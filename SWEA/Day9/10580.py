#전봇대
#https://velog.io/@daeungdaeung/SWEA-10580-%EC%A0%84%EB%B4%87%EB%8C%80with-Python
from itertools import combinations
T=int(input())
for tc in range(1,T+1):
  n=int(input())
  lines=[]
  ans=0
  for _ in range(n):
    l,r=map(int,input().split())
    lines.append([l,r])

  comb=list(combinations(lines,2))
  for c in comb:
    l1,l2=c
    l1l,l1r=l1[0],l1[1]
    l2l,l2r=l2[0],l2[1]
    if (l1l<l2l and l1r>l2r) or (l2l<l1l and l2r>l1r): #겹치면
      ans+=1

      
    
  print(f'#{tc} {ans}')