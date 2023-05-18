#내 풀이->테스트 통과 DATE=>5.18 풀이시간10분
import heapq
def cookies(k, A):
    # Write your code here
    q=[]
    for a in A:
        heapq.heappush(q,a)
    cnt=0
    while len(q)>=2 and q[0]<k:
        cnt+=1
        c1=heapq.heappop(q)
        c2=heapq.heappop(q)
        heapq.heappush(q,c1+2*c2)
    if q[0]>=k:
        return cnt
    else:
        return -1
        