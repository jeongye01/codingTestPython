#[S/W 문제해결 응용] 2일차 - 최대 상금
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 40분 
from itertools import combinations


T = int(input())
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    ans=0
    array=list(str(n))
    idxs=[0]*len(array)
    for i in range(len(array)):
      idxs[i]=i
    #두개를 뽑는 모든 조합
    comb = list(combinations(idxs, 2))
    prod=[]
    # i개의 조합에서만 위치 변경되는 경우 pick
    for i in range(1,m+1):
      prod=prod+list(combinations(comb, i))
    result=[]
    # 각 경우에 대해서 result 도출
    for p in prod:
      tmp=array[:]
      for i in range(m):
        c=p[i%len(p)]
        tmp[c[0]],tmp[c[1]]= tmp[c[1]],tmp[c[0]]
      result.append(''.join(tmp))
      
      
    # 가장 큰 값 
    ans=max(result)

    print("#{} {}".format(test_case,ans))
