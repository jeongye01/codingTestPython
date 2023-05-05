#상호의 배틀필드
##내 풀이->테스트 통과 DATE=>5.5 풀이시간 100분 
dm = {"U": 0, "L": 1, "D": 2, "R": 3}
dm2 = {"^": 0, "<": 1, "v": 2, ">": 3}
dm3 = {0: "^", 1: "<", 2: "v", 3: ">"}


def findCar():
  global direction, x, y, board
  for i in range(h):
    for j in range(w):
      if (board[i][j] == "^" or board[i][j] == "<" or board[i][j] == "v"
          or board[i][j] == ">"):
        direction = dm2[board[i][j]]
        x, y = j, i
        board[i][j] = "."
        return


def posCar(x, y):
  global board
  board[y][x] = dm3[direction]


T = int(input())
for tc in range(1, T + 1):
  #모든 입력을 처리하고 나면 게임 맵의 상태가 어떻게 되는지
  h, w = map(int, input().split())
  board = [list(input()) for _ in range(h)]
  n = int(input())
  ui = input()
  dx = [0, -1, 0, 1]
  dy = [-1, 0, 1, 0]
  direction = 0
  x, y = 0, 0
  findCar()
  #move={"U":(0,-1),"D":(0,1),"L":(-1,0),"R":(1,0),"S":(0,0)}
  for i in range(n):
    move = ui[i]

    if (move == "S"):
      nx, ny = x + dx[direction], y + dy[direction]
      while 0 <= nx < w and 0 <= ny < h:
        #print(nx,ny,x,y,direction)
        if (board[ny][nx] == "*"):
          board[ny][nx] = "."
          break
        if (board[ny][nx] == "#"):
          break
        nx += dx[direction]
        ny += dy[direction]

      continue

    direction = dm[move]
    nx, ny = x + dx[direction], y + dy[direction]
    if (0 <= nx < w and 0 <= ny < h and board[ny][nx] == "."):
      x, y = nx, ny

  posCar(x, y)

  print("#{}".format(tc), end=" ")
  for row in board:
    for col in row:
      print(col, end="")
    print()