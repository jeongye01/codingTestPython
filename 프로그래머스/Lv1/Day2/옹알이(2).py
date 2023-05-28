#https://school.programmers.co.kr/learn/courses/30/lessons/133499/solution_groups?language=python3
##내 풀이->테스트 통과 DATE=>5.28 풀이시간 40분 
def solution(babbling):
    answer = 0
    can=["aya", "ye", "woo", "ma"]
    for bab in babbling:
        tmp=bab
        repeat=False
        last = ""
        while tmp:
            match=False
            for c in can:
                if tmp.find(c)==0:
                   if last==c:
                        repeat=True
                   last=c
                   match=True
                   break
            if match:
                if repeat:
                    break
                tmp=tmp[len(last):]
                if tmp=="":
                    answer+=1
            else:
                break
    return answer


'''

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer


'''