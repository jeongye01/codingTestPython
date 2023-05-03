# N-Queen
# 내풀이아님
# backtracking 알고리즘 대표 유형
def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == abs(x - i):
            return False
    return True
     
def backtracking(depth):
    global answer
    if depth == n:
        answer += 1
        return
    for i in range(n):
        visited[depth] = i
        if check(depth):
            backtracking(depth + 1)            
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    answer = 0 
    visited = [0] * n
    backtracking(0)
    print('#{} {}'.format(tc, answer))