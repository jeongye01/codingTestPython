#달팽이 숫자
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 18분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    board=[[0]*n for _ in range(n)]
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    d=3 #감소하는 방향으로 가면됨
    x,y=-1,0
    for i in range(1,n*n+1):
      
      nx,ny=x+dx[d],y+dy[d]
      if(nx<0 or nx>=n or ny<0 or ny>=n or board[ny][nx]!=0):
        d=(d-1) if d-1>=0 else 3
        nx,ny=x+dx[d],y+dy[d]
      board[ny][nx]=i
      x,y=nx,ny
    

    print("#{}".format(test_case))
    for r in board:
      for c in r:
        print(c,end=" ")
      print()