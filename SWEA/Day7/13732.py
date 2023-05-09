# 정사각형 판정
'''
더 괜찮은 풀이


'''
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 50분 
T = int(input())

def check(x,y):
  global ans
  length=0
  nx=x
  q=sharpCtn
  while True:
    if nx<n and board[y][nx]=="#":
      length+=1
      nx+=1
      q-=1
    else:
      break
  
  if length==1 or length+y>n:
    ans="no"
    return 
  for i in range(y+1,length+y):
    tmp=0
    nx=x
    while True:
      if nx<n and board[i][nx]=="#":
        tmp+=1
        nx+=1
        q-=1
      else:
        break
    if tmp!=length:
      ans="no"
      return
  if q!=0:
    ans="no"
    
def findSharp():
  global x,y,sharpCtn
  for i in range(n):
    for j in range(n):
      if(board[i][j]=="#"):
        if(x==-1 and y==-1):
          x=j
          y=i
        sharpCtn+=1
    
for tc in range(1,T+1):
  n=int(input())
  board=[]
  for i in range(n):
    board.append(list(input()))
  ans="yes"
  x,y=-1,-1
  sharpCtn=0
  findSharp()
  check(x,y)
  if sharpCtn==1:
    ans="yes"
  print(f"#{tc}",ans)