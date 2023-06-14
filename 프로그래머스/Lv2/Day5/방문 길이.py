#https://school.programmers.co.kr/learn/courses/30/lessons/49994
#내 풀이->테스트 통과 DATE=>6.14 풀이시간 20분 
def solution(dirs):
    answer = []
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    dd={"U":0,"D":2,"R":3,"L":1}
    x,y=0,0
    for i in dirs:
        nx,ny=x+dx[dd[i]],y+dy[dd[i]]
        if -5<=nx<=5 and -5<=ny<=5:
            way={(x,y),(nx,ny)}
            if way not in answer:
                answer.append({(x,y),(nx,ny)})
            x, y = nx, ny
    return len(answer)