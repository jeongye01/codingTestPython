#https://school.programmers.co.kr/learn/courses/30/lessons/42840
#내 풀이->테스트 통과 DATE=>5.29 풀이시간 10분 
def solution(answers):
    answer = []
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    p1=0
    p2=0
    p3=0
    for i,a in enumerate(answers):
        if a==a1[i%len(a1)]:
            p1+=1
        if a==a2[i%len(a2)]:
            p2+=1
        if a==a3[i%len(a3)]:
            p3+=1
    mx=max([p1,p2,p3])
    for p in [1,2,3]:
        if [p1,p2,p3][p-1]==mx:
            answer.append(p)
        
    return answer