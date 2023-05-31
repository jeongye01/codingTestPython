#https://school.programmers.co.kr/learn/courses/30/lessons/12930
###내 풀이->테스트 통과 DATE=>6.1 풀이시간 5분 
def solution(s):
    answer = ''
    o=-1
    for i,x in enumerate(s):
        if x==" ":
            o=-1
            answer+=" "
            continue
        o+=1
        if o%2==0:
            answer+=x.upper()
        else:
            answer+=x.lower()
    return answer