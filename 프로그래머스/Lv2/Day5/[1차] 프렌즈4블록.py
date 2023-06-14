#https://school.programmers.co.kr/learn/courses/30/lessons/17679
##내 풀이->테스트 통과 DATE=>6.14 풀이시간 70분 
import copy
def solution(m, n, board):
    answer = 0
    dx=[0,1,1,0]
    dy=[1,0,1,0]
    board=[list(item) for item in board]
    for b in board:
        print(*b)
    while True:
        cnt=0
        board2 = copy.deepcopy(board)
        for i in range(m-1):
            for j in range(n-1):
                c=board[i][j]
                if c!="0":
                    match=True
                    for d in range(3):
                        nx,ny=j+dx[d],i+dy[d]
                        if board[ny][nx]!=c:
                            match=False
                            break
                    if match:
                        for d in range(4):
                            nx, ny = j + dx[d], i + dy[d]
                            board2[ny][nx]='x'

        for c in range(n):
            col = ''
            for r in range(m):
                if board2[r][c]=='x':
                    cnt+=1
                col+=board2[r][c]
            col=col.replace('x','')
            col='0'*(m-len(col))+col
            for r in range(m):
                board[r][c]=col[r]

        if cnt==0:
            break
        answer += cnt

    return answer