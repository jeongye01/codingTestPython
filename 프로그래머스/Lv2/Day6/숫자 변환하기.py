#https://school.programmers.co.kr/learn/courses/30/lessons/154538
#https://studyposting.tistory.com/93
def solution(x, y, n):
    DP = [int(1e9) for _ in range(y + 1)]
    DP[x] = 0
    for i in range(x, y + 1):
        if i + n <= y:
            DP[i+n] = min(DP[i + n], DP[i] + 1)
        if i * 2 <= y:
            DP[i*2] = min(DP[i * 2], DP[i] + 1)
        if i * 3 <= y:
            DP[i*3] = min(DP[i * 3], DP[i] + 1)
    return DP[y] if DP[y]!=int(1e9) else -1