#https://school.programmers.co.kr/learn/courses/30/lessons/17686
#내 풀이->테스트 통과 DATE=>6.14 풀이시간 30분 
def solution(files):
    answer = []
    sf=[]
    for f in files:
        head=""
        number=""
        tail=""
        for x in f:
            if ord('0')<=ord(x)<=ord('9') and not tail:
                number+=x
            elif not number:
                head+=x
            else:
                tail+=x
        sf.append([head,number,tail])
    sf.sort(key=lambda x:(x[0].lower(),int(x[1])))

    for f in sf:
        answer.append("".join(f))
    return answer