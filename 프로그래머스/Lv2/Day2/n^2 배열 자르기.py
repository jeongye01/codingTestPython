#https://school.programmers.co.kr/learn/courses/30/lessons/87390
#내 풀이->테스트 통과 DATE=>6.4 풀이시간 40분 
def solution(n, left, right):
    answer=[]
    if left//n == right//n:
        for c in range(left % n, right % n + 1):
            if c <= left // n:
                answer.append(left // n + 1)
            else:
                answer.append(c + 1)
    else:
        for c in range(left % n, n):
            if c <= left // n:
                answer.append(left // n + 1)
            else:
                answer.append(c + 1)
        for r in range(left // n + 1, right // n):
            for c in range(0, n):
                if c <= r:
                    answer.append(r + 1)
                else:
                    answer.append(c + 1)
        for c in range(right % n + 1):
            if c <= right // n:
                answer.append(right // n + 1)
            else:
                answer.append(c + 1)
    return answer

'''
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer


'''