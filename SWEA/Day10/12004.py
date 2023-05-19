#구구단 1
#내 풀이->테스트 통과 DATE=>5.19 풀이시간 3분 
from itertools import product
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    comb=list(product([i for i in range(1,10)],repeat=2))
    ans="No"
    for c in comb:
        a,b=c
        if a*b==n:
            ans="Yes"
            break
    print(f"#{tc} {ans}")