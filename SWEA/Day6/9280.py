# 진용이네 주차타워
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 50분 
from collections import deque
import heapq
T = int(input())
for tc in range(1,T+1):
  ans=0 #진용이가 오늘 하룻동안 벌어들일 수입
  n,m=map(int,input().split())
  rq=[]
  ws=[]
  record=[]
  for i in range(n):
    heapq.heappush(rq,(i,int(input())))
  for _ in range(m):
    ws.append(int(input()))
  for _ in range(2*m):
    record.append(int(input()))
  wating=deque([])
  states=[0]*m
  for i in range(2*m):
    if(record[i]>0):
      if(rq):
        idx,r=heapq.heappop(rq)
        ans+=ws[record[i]-1]*r
        states[record[i]-1]=(idx,r)
      else:#대기해야함.
        wating.append(record[i])
    else:
      if(wating):
        w=wating.popleft()
        ans+=ws[w-1]*states[record[i]*-1-1][1]
        states[w-1]=states[record[i]*-1-1]
      else:
        heapq.heappush(rq,states[record[i]*-1-1])
  print(f"#{tc}",ans)