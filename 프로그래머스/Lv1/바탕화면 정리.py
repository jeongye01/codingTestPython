#https://school.programmers.co.kr/learn/courses/30/lessons/161990
##내 풀이->테스트 통과 DATE=>5.27 풀이시간 50분 
def solution(wallpaper):
    x,y=[],[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=="#":
                x.append(j)
                y.append(i)
                
   
    
    return [min(y),min(x),max(y)+1,max(x)+1]