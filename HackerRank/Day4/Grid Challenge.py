###내 풀이->테스트 통과 DATE=>5.14 풀이시간 10분
def gridChallenge(grid):
    # Write your code here
    for g in grid:
        g.sort()
    cn=len(grid[0])
    for c in range(cn):
        for r in range(1,n):
            if ord(grid[r-1][c])>ord(grid[r][c]):
                return "NO"
    return "YES"