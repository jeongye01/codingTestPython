# https://school.programmers.co.kr/learn/courses/30/lessons/64061#
###내 풀이->테스트 통과 DATE=>5.29 풀이시간 10분 
def solution(board, moves):
    answer = 0
    n = len(board)
    newBoard = []
    for i in range(n):
        col = []
        for j in range(n - 1, -1, -1):
            if board[j][i] != 0:
                col.append(board[j][i])
        newBoard.append(col)
    bucket = []
    for m in moves:
        if not newBoard[m-1]:
            continue
        d = newBoard[m - 1].pop()
        if len(bucket) and bucket[-1] == d:
            bucket.pop()
            answer += 2
        else:
            bucket.append(d)

    return answer