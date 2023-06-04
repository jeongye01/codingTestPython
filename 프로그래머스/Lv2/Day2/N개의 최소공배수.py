#https://school.programmers.co.kr/learn/courses/30/lessons/12953
#내 풀이->테스트 통과 DATE=>6.4 풀이시간 15분 
def solution(arr):
    arr.sort()
    mx=arr[-1]
    m=1
    while True:
        success=True
        for a in arr:
            if mx%a!=0:
                success=False
                break
        if success:
            break
        else:
            m+=1
            mx=m*arr[-1]
    return mx