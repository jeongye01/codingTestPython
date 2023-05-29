#https://school.programmers.co.kr/learn/courses/30/lessons/77884
###내 풀이->테스트 통과 DATE=>5.29 풀이시간 1분 
def solution(left, right):
    answer = 0
    for n in range(left,right+1):
        cnt=0
        for i in range(1,n+1):
            if n%i==0:
                cnt+=1
        answer+=(n if cnt%2==0 else -1*n)
    return answer


'''

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'''