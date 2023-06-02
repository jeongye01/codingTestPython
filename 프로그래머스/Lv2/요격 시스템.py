#https://velog.io/@mang0206/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9A%94%EA%B2%A9-%EC%8B%9C%EC%8A%A4%ED%85%9C-python

def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])

    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer