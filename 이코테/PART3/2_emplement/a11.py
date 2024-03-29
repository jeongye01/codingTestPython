#뱀
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보
# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))
# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시 direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
            # 벽이나 뱀의 몸통과 부딪혔다면
            else:
                time += 1
                break
            x, y = nx, ny # 다음 위치로 머리를 이동
            time += 1
            if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
                direction = turn(direction, info[index][1])
                index += 1
    return time
print(simulate())










'''
#내풀이->테스트통과  DATE->4.16 풀이시간->180분
from collections import deque



n=int(input())
k=int(input())
array=[[0]*n for _ in range(n)]

for _ in range(k):
  row,col=map(int,input().split())
  array[row-1][col-1]=1

inst_deque=[]
t=int(input())


inst_array=deque()
for _ in range(t):
   sec,dir=input().split()
   inst_array.append((sec,dir))

dx=[0,-1,0,1]
dy=[-1,0,1,0]
di=3
x,y=0,0

snake=deque()
snake.appendleft((x,y))
result=-1 # 몇 초에 끝나는지
prev=0

inst=inst_array.popleft()
sec,dir=inst[0],inst[1]
while True:
  result+=1
  
  if(result==int(sec)):
    if(dir=="D"):
       di=di-1 if di-1>=0 else 3
    else:
       di=(di+1)%4
    if len(inst_array):
      inst=inst_array.popleft()
      sec,dir=inst[0],inst[1]



  x,y=x+dx[di],y+dy[di]

  if( x<0 or x>=n or y<0 or y>=n):
      break;
  if((x,y) in snake):
      break
  snake.append((x,y))
  if(array[y][x]==1): #사과있음
    array[y][x]=0
  else:
    snake.popleft()

print(result+1)
'''

'''
#내풀이->테스트통과  DATE->5.18 풀이시간->70분
from collections import deque
n=int(input())
k=int(input())
board=[[0]*(n+2) for _ in range(n+2)]
for _ in range(k):
    r,c=map(int,input().split())
    board[r][c]=1 # 사과 배치
l=int(input())
move=deque()
for _ in range(l):
    s,d=input().split()
    move.append((int(s),d))
dx=[0,-1,0,1]
dy=[-1,0,1,0]
direction=3
time=0
x,y=1,1 #머리 위치
snake=deque([(x,y)])
isEnd=False
prev=0
idx=0
while True:
    if move:
        s,d=move.popleft()
    else:
        s=10000
        prev=0
    for t in range(s-prev):
        time += 1
        x,y=x+dx[direction],y+dy[direction] # 머리 위치 이동
        if x<1 or x>n or y<1 or y>n or ((x,y) in snake):
            #print("왜?",x,y,snake)
            isEnd=True
            break
        snake.append((x, y))
        if board[y][x]!=1: #사과가 없다면
            snake.popleft()
        else:
            board[y][x]=0

        #print("-----!-----",snake)


    if isEnd:
        break
    prev=s
    if d=="L":
        direction=(direction+1)%4
        #print(d,direction,(direction-1)%4)
    elif d=="D":
        direction=(direction-1)%4

print(time)

'''