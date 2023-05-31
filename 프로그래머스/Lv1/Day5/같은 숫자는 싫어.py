#https://school.programmers.co.kr/learn/courses/30/lessons/12906
####내 풀이->테스트 통과 DATE=>6.1 풀이시간 3분 
def solution(arr):
    answer=[]
    flag=arr[0]
    for a in arr[1:]:
        if flag==a:
            continue
        else:
            answer.append(flag)
            flag=a
    answer.append(flag)
        
    return answer