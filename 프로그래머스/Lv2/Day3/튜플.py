#https://school.programmers.co.kr/learn/courses/30/lessons/64065
#내 풀이->테스트 통과 DATE=>6.5 풀이시간 15분 
def solution(s):
    answer =[]
    nd={}
    tmp=""
    for x in s:
        if ord('0')<=ord(x)<=ord('9'):
            tmp += x
        elif tmp:
            if int(tmp) in nd:
                nd[int(tmp)]+=1
            else:
                nd[int(tmp)]=1
            tmp=""
    nd=sorted(nd.items(), key=lambda x: x[1],reverse=True)
    for n in nd:
        answer.append(n[0])
    return answer