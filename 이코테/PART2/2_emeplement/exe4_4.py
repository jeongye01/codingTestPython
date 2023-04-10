# 게임개발
n,m=map(int,input().split())
a,b,d=map(int,input().split())
mapArr = [list(map(int, input().split())) for _ in range(m)]
memoryArr=[[0] * m for i in range(n)]
#0북쪽,1동쪽,2남쪽,3서쪽
turnOrder=[[3,2,1,0],[0,3,2,1],[1,0,3,2],[2,1,0,3]]
moveMap=[(-1,0),(0,1),(1,0),(0,-1)]

#0육지,1바다


ans=0
canMove=True

while(canMove):
  
  isDetectedNext=False
  if(not(memoryArr[a][b])):
    ans+=1
    memoryArr[a][b]=1 #방문 표시 
  for i in range(4):# 반시계방향 회전. 방문기록 없는 칸 탐색
    tempA=a+moveMap[turnOrder[d][i]][0]
    tempB=b+moveMap[turnOrder[d][i]][1]
    isOutSide=tempA<0 or tempA>n or tempB<0 or tempB>m
    if(not(isOutSide) and not(memoryArr[tempA][tempB])): # 방문기록 없는 칸 발견
      if(mapArr[tempA][tempB]): #바다인 경우
        continue
      else: #육지인 경우, 이동 할 칸 찾음
        d=turnOrder[d][i] #방향 조정
        a,b=tempA,tempB #이동
        isDetectedNext=True
        break
  
  if(not(isDetectedNext)): # 이동할 칸 못 찾음
    #뒤 칸이 바다인지 확인
    backA=a+moveMap[turnOrder[d][1]][0]
    backB=b+moveMap[turnOrder[d][1]][1]
    if(mapArr[backA][backB]):
      canMove=False
    else:
      a,b=backA,backB #뒤로 이동
    
  
  
print(ans)