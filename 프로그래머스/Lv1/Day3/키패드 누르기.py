#https://school.programmers.co.kr/learn/courses/30/lessons/67256
#내 풀이->테스트 통과 DATE=>5.29 풀이시간 30분 
import math

def check(x,n):
    for d in [-3,3,+1,-1,0]:
        if x+d==n:
            return True
    return False

def solution(numbers, hand):
    answer = ''
    l, r = 10,12
    for n in numbers:
        now=""
        if n in [1, 4, 7]:
            now="L"
        elif n in [3, 6, 9]:
            now="R"
        else:
            if n==0:
                n=11

            if (check(r,n) and check(l,n)) or (not check(r,n) and not check(l,n)):
                rd = abs((n - 1) % 3 - (r - 1) % 3) + abs(math.ceil(n / 3) - math.ceil(r / 3))
                ld = abs((n - 1) % 3 - (l - 1) % 3) + abs(math.ceil(n / 3) - math.ceil(l / 3))
                if rd < ld:
                    now="R"
                elif rd > ld:
                    now="L"
                else:
                    if hand == "right":
                        now="R"
                    else:
                        now="L"
            elif check(r,n):
                now="R"
            else:
                now="L"
        answer+=now
        if now=="R":
            r=n
        else:
            l=n



    return answer