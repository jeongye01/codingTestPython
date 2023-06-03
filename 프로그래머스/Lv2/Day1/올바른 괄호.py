#https://school.programmers.co.kr/learn/courses/30/lessons/12909
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 5분 
def solution(s):
    cnt=0
    for x in s:
        if x=="(":
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            break

    return cnt==0