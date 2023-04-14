# 문자열 압축
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

        

'''
#내풀이->테스트통과  DATE->4.12 풀이시간->57분
def solution(s):
    answer = 0 #표현한 문자열 중 가장 짧은 것의 길이
    length=len(s)
    new_s=[]
    gap=0
    while(gap<=(length//2)):
        temp=""
        gap+=1
        cnt=1
        focus=s[0:gap]
        for i in range(gap,length,gap):
                if(s[i:i+gap]==focus):
                    cnt+=1
                else:
                    temp += str(cnt) + focus if cnt >= 2 else focus
                    cnt=1
                    focus=s[i:i+gap]
        temp += str(cnt) + focus if cnt >= 2 else focus
        if(len(temp)>0):
          new_s.append(len(temp))

    answer=min(new_s)
    return answer

'''
