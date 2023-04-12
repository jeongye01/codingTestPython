#내풀이 DATE->4.12 풀이시간->40분
n, m = map(int, input().split())
x, y, d = map(int, input().split())
mapArr = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ctn = 0
result = 1


def move(newX,newY):
  global mapArr, x, y, result
  mapArr[y][x] = -1
  x, y = newX, newY
  result += 1


while True:

  tempX, tempY = x + dx[d], y + dy[d]
  if (tempX >= 0 and tempX < n and tempY >= 0 and tempY < m
      and mapArr[tempY][tempX] == 0):
    move(tempX,tempY)
    ctn = 0

  else:
    d = (d + 1) % 4
    ctn += 1

  if (ctn == 4):
    back = (d + 1) % 4
    tempX, tempY = x - dx[back], y - dy[back]
    if (mapArr[tempY][tempX] == 1):  #뒤가 바다
      break
    else:
      move(tempX,tempY)

print(result)


'''
#내 풀이  3.20
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
'''