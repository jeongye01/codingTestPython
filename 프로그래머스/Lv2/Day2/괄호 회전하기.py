#https://school.programmers.co.kr/learn/courses/30/lessons/76502
#내 풀이->테스트 통과 DATE=>6.4 풀이시간 20분 
def solution(s):
    answer = 0
    if len(s)%2==1:
        return 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        op = {"(", "[", "{"}
        match = {")": "(", "]": "[", "}": "{"}
        answer += 1
        open = []
        for x in s:
            if x in op:
                open.append(x)
            elif open and open[-1] == match[x]:
                open.pop()
            else:
                answer -= 1
                break

    return answer