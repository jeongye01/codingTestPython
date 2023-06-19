#https://school.programmers.co.kr/learn/courses/30/lessons/132265
#https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A1%A4%EC%BC%80%EC%9D%B4%ED%81%AC-%EC%9E%90%EB%A5%B4%EA%B8%B0
from collections import Counter
def solution(topping):
    answer = 0
    topps = Counter(topping)
    top_set = set() # 철수꺼 
    
    for top in topping:
        top_set.add(top)
        topps[top] -= 1
        
        if topps[top] == 0:
            topps.pop(top)
        if len(topps) == len(top_set):
            answer += 1
        
    return answer