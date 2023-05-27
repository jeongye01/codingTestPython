#https://school.programmers.co.kr/learn/courses/30/lessons/172928
#공원 산책
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 120분 
dx=[0,-1,0,1]
dy=[-1,0,1,0]
def findStart(park):
    for r in range(len(park)):
        for c in range(len(park[0])):
                if park[r][c]=="S":
                    return (c,r)
def check(x,y,d,nx,ny,park):
    xx,yy=x,y
    while min(x,nx)<=xx<=max(x,nx) and min(y,ny)<=yy<=max(y,ny):
        if park[yy][xx]=='X':
            return False
        xx,yy=xx+dx[d],yy+dy[d]

    return True
def solution(park, routes):
    x,y=findStart(park)
    d={"N":0,"E":3,"S":2,"W":1}
    for route in routes:
        direction=d[route[0]]
        nx,ny=x+dx[direction]*int(route[-1]),y+dy[direction]*int(route[-1])
        if 0<=nx<len(park[0]) and 0<=ny<len(park):
            if check(x,y,direction,nx,ny,park):
                x,y=nx,ny

    return [y,x]