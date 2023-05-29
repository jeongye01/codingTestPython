#https://school.programmers.co.kr/learn/courses/30/lessons/118666
##내 풀이->테스트 통과 DATE=>5.28 풀이시간 20분 
def solution(survey, choices):
    answer = ''
    res=dict({"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0})
    p=[-1,3,2,1,0,1,2,3]
    for i,c in enumerate(choices):
        if c>3:
            res[survey[i][1]]+=p[c]
        else:
            res[survey[i][0]]+=p[c]
    table=["RT","CF","JM","AN"]
    for t in table:
        if res[t[0]]<res[t[1]]:
            answer+=t[1]
        else:
            answer+=t[0]
    return answer