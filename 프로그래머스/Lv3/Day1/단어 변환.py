#https://school.programmers.co.kr/learn/courses/30/lessons/43163
##내 풀이->테스트 통과 DATE=>6.27 풀이시간 15분 
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    wd={key:0 for key in words+[begin]}
    q=deque([begin])
    n=len(words[0])
    while q:
        now=q.popleft()
        for word in words:
            if wd[word]==0:
                cnt=0
                for i in range(n):
                    if word[i]!=now[i]:
                        cnt+=1
                if cnt==1:
                    wd[word]=wd[now]+1
                    q.append(word)

    
    return wd[target]