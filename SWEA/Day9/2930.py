#힙
#내 풀이->테스트 통과 DATE=>5.17 풀이시간 20분 
import heapq

T=int(input())
for tc in range(1,T+1):
  n=int(input())
  result=[]
  q=[]
  opes=[]
  for _ in range(n):
    opes.append(input())
  
  for ope in opes:
    if ope[0]=='1':
      o,x=ope.split()
      heapq.heappush(q,-int(x))
    else:
      if q:
        p=heapq.heappop(q)
        result.append(p)
      else:
        result.append(1)
    
  #print(result,"Res")
  print('#{}'.format(tc),end=" ")
  for r in result:
    print(r*(-1),end=" ")
  print()