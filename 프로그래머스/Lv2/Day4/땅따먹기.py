#https://school.programmers.co.kr/learn/courses/30/lessons/12913
#https://latte-is-horse.tistory.com/229
def solution(land):
    answer = 0
    m = len(land)
    d = [[i for i in land[0]]]
    d.extend([[0]*4 for _ in range(m-1)])
    for i in range(1, m):
        for j in range(4):
            a, b, c = [jj for jj in range(4) if jj != j]
            d[i][j] = land[i][j] + max(d[i-1][a], d[i-1][b], d[i-1][c])

    return max(d[-1])