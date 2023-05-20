# https://velog.io/@good_da22/SW-Expert-Academy-D3-10965%EB%B2%88-%EC%A0%9C%EA%B3%B1%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0python
# 제곱수 만들기
prime = [2]
for i in range(3, int(10000000 ** 0.5), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)
 
ans = []
T = int(input())
for tc in range(1, T + 1):
    A = int(input())
    res = 1
    if A ** 0.5 != int(A**0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    ans.append('#{} {}'.format(tc, res))
for n in ans:
    print(n)