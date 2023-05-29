#https://school.programmers.co.kr/learn/courses/30/lessons/92334
##내 풀이->테스트 통과 DATE=>5.28 풀이시간 20분 
def solution(id_list, report, k):
    answer = []
    send = dict()
    receive = dict()
    for id in id_list:
        send[id] = set()
        receive[id] = set()
    for p in report:
        s, r = map(str, p.split())
        send[s].add(r)
        receive[r].add(s)
    for id in id_list:
        tmp = 0
        for r in list(send[id]):
            if len(receive[r]) >= k:
                tmp += 1
        answer.append(tmp)

    return answer