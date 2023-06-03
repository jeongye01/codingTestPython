#https://school.programmers.co.kr/learn/courses/30/lessons/12941
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 5분 
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]

    return answer