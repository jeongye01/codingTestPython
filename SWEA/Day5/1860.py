#진기의 최고급 붕어빵
#내 풀이->테스트 통과 DATE=>5.6 풀이시간 40분 
from collections import deque
T = int(input())

for tc in range(1, T + 1):
  ans="Possible" #모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 “Possible”을, 아니라면 “Impossible”을 출력한다.
  n,m,k=map(int,input().split())
  data=sorted(list(map(int,input().split()))) #언제 도착하는지 
  data=deque(data)

  # 주의 ! 동시도착 손님
  left=0 #붕어빵재고
  latest=max(data) #제일 늦게 오는 시간
  for i in range(0,latest+1):
    if(i>0 and i%m==0):
      left+=k
    while(len(data)>0 and data[0]==i):
      p=data.popleft()
      if(left>0):
        left-=1
      else:
        ans="Impossible"
        break
    

  print(f"#{tc} {ans}")
