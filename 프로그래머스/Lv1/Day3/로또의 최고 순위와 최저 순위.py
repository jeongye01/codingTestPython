#https://school.programmers.co.kr/learn/courses/30/lessons/77484
###내 풀이->테스트 통과 DATE=>5.29 풀이시간 10분 
def solution(lottos, win_nums):
    pm=0
    nm=0
    for i,lotto in enumerate(lottos):
        if lotto in win_nums:
            nm+=1
            pm+=1
        elif lotto==0:
            pm+=1
    best=6-pm+1
    worst=6-nm+1
    return [best if best<=6 else 6,worst if worst<=6 else 6]