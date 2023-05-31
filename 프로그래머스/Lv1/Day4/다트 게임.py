#https://school.programmers.co.kr/learn/courses/30/lessons/17682
##내 풀이->테스트 통과 DATE=>6.1 풀이시간 30분 
def solution(dartResult):
    pw={"S":1,"D":2,"T":3}
    p=""
    q=[]
    for d in dartResult:
        if ord('0')<=ord(d)<=ord('9'):
            p+=d
        elif d in pw:
            q.append(pow(int(p),pw[d]))
            p=""
        elif d=="#":
            q[-1]=q[-1]*-1
        else:
            q[-1]=q[-1]*2
            if len(q)>=2:
                q[-2]=q[-2]*2
    return sum(q)