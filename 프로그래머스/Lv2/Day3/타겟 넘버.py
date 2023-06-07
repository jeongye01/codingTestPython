#https://school.programmers.co.kr/learn/courses/30/lessons/43165
##내 풀이->테스트 통과 DATE=>6.5 풀이시간 15분 
ans = 0
def bt(idx, target, summary, numbers):
    global ans
    if idx == len(numbers):
        if summary == target:
            ans += 1
        return
    bt(idx + 1, target, summary + numbers[idx], numbers)
    bt(idx + 1, target, summary - numbers[idx], numbers)


def solution(numbers, target):
    bt(0, target, 0, numbers)

    return ans