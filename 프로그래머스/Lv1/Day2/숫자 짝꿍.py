#https://school.programmers.co.kr/learn/courses/30/lessons/131128
##내 풀이->테스트 통과 DATE=>5.28 풀이시간 10분 
def solution(X, Y):
    answer = ''
    mx=[0]*10
    my=[0]*10
    for x in X:
        mx[int(x)]+=1
    for y in Y:
        my[int(y)]+=1
    for i in range(9,-1,-1):
        answer+=str(i)*min(mx[i],my[i])
    if answer=="":
        answer="-1"
    if answer[0]=="0":
        answer="0"
    return answer
'''
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
'''