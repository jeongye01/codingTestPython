#숫자가 같은 배수
#내 풀이->테스트 통과 DATE=>5.14 풀이시간 6분 
from itertools import permutations

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    nrr=list(str(n))
    perm=list(permutations(nrr,len(nrr)))
    ans='impossible'
    for p in perm:
        tmp=int("".join(list(p)))
        if tmp>n and tmp%n==0:
            ans="possible"
            break


    print(f"#{tc} {ans}")