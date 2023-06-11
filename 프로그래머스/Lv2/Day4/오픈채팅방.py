#https://school.programmers.co.kr/learn/courses/30/lessons/42888
#내 풀이->테스트 통과 DATE=>6.11 풀이시간 10분 
def solution(record):
    answer = []
    nd={}
    word={"Enter":"님이 들어왔습니다.","Leave":"님이 나갔습니다."}
    for r in record:
        rl=r.split()
        if len(rl)==3:
            nd[rl[1]]=rl[2]

    for r in record:
        rl=r.split()
        if rl[0] in word:
            answer.append(f"{nd[rl[1]]}{word[rl[0]]}")

    return answer