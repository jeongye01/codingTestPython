# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        cnt=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                cnt+=2 if i**2!=n else 1
        answer+=(cnt if cnt<=limit else power)                
    return answer