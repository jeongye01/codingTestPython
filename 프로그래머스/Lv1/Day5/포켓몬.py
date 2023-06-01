#https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
###내 풀이->테스트 통과 DATE=>6.1 풀이시간 5분 
def solution(nums):
    return len(set(nums)) if len(set(nums))<=len(nums)//2 else len(nums)//2