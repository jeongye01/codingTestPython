#https://school.programmers.co.kr/learn/courses/30/lessons/42884
##내 풀이->테스트 통과 DATE=>6.28 풀이시간 40분 
def solution(routes):
    routes.sort(key=lambda x:(x[0],x[1]))
    ed = routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        if ed>=routes[i][0]:
            ed=min(routes[i][1],ed)
        else:
            ed =  routes[i][1]
            answer+=1


    return answer