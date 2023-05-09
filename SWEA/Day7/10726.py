#이진수 표현
#내 코드 아님
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flag = True
    answer = 'ON'
    for i in range(n):
        if m % 2 == 0:
            flag = False
            break
        else:
            m //= 2
    if not flag:
        answer = 'OFF'
    r = '#{} {}'.format(test_case, answer)
    print(r)