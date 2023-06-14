#https://school.programmers.co.kr/learn/courses/30/lessons/84512
#내 풀이->테스트 통과 DATE=>6.14 풀이시간 15분 
#심심해서 이렇게 풀음
def solution(word):
    answer = 0
    wd=[ 'A', 'E', 'I', 'O', 'U']
    for a in range(5):
        answer += 1
        if wd[a]==word:
            return answer
        for b in range(5):
            answer += 1
            if wd[a]+wd[b]==word:
                return answer
            for c in range(5):
                answer += 1
                if wd[a]+wd[b]+wd[c]==word:
                    return answer
                for d in range(5):
                    answer += 1
                    if wd[a]+wd[b]+wd[c]+wd[d]==word:
                        return answer
                    for e in range(5):
                        answer += 1
                        if wd[a]+wd[b]+wd[c]+wd[d]+wd[e]==word:
                            return answer
    return answer