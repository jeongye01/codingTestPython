#https://school.programmers.co.kr/learn/courses/30/lessons/142086
##내 풀이->테스트 통과 DATE=>5.27 풀이시간 10분 
def solution(s):
    answer = []
    chrs = [-1] * 26
    for i, x in enumerate(s):
        idx = ord(x) - ord('a')
        answer.append(-1 if chrs[idx] == -1 else i - chrs[idx])
        chrs[idx] = i

    return answer