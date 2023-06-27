#https://school.programmers.co.kr/learn/courses/30/lessons/42628
#https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99
import heapq
def solution(operations):
    q=[]
    for o in operations:
        o1, o2 = o.split()
        if o1=="I":
            heapq.heappush(q,int(o2))
        elif q:
            if o2=="1":
                q.remove(max(q))
            else:
                heapq.heappop(q)
    if q:
        return [max(q),min(q)]
    return [0,0]