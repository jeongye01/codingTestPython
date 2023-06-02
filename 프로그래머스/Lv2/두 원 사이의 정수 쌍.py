#https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%EC%9B%90-%EC%82%AC%EC%9D%B4%EC%9D%98-%EC%A0%95%EC%88%98-%EC%8C%8D
#https://school.programmers.co.kr/learn/courses/30/lessons/181187
def solution(r1, r2):
    answer = 0
    minY, maxY = r1,r2 #최소, 최대로 가질 수 있는 y좌표
    # 1사분면에 대해서만 좌표값을 구하고 대칭이므로 *4한다.
    for x in range(0,r2):
        while r2**2 < maxY**2 + x**2:
            maxY -= 1
        # minY 양수값을 유지 
        while minY-1 and r1**2 <= (minY-1)**2 + x**2:
            minY -= 1
        answer += (maxY-minY) + 1
    
    return answer*4