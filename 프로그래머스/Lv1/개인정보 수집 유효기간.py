#https://school.programmers.co.kr/learn/courses/30/lessons/150370
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 20분 
def solution(today, terms, privacies):
    answer = []
    terms_dict={term.split()[0]:int(term.split()[-1])*28 for term in terms}
    for i,p in enumerate(privacies):
        now=int(today.split(".")[0])*28*12+int(today.split(".")[1])*28+int(today.split(".")[2][0:2])
        prev=int(p.split(".")[0])*28*12+int(p.split(".")[1])*28+int(p.split(".")[2][0:2])
        if now-prev>=terms_dict[p[-1]]:
            answer.append(i+1)
    return answer


'''
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire



'''