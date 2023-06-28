#https://school.programmers.co.kr/learn/courses/30/lessons/12979
#https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B8%B0%EC%A7%80%EA%B5%AD-%EC%84%A4%EC%B9%98-SummerWinter-Coding2018-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python

from math import ceil

def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1
    
    start = 1
    for s in stations:
        answer += max(ceil((s - w - start) / W), 0)
        start = s + w + 1
        
    if n >= start:
        answer += ceil((n - start + 1) / W)
    
    return answer