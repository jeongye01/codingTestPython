#외로운 문자
#내 풀이->테스트 통과 DATE=>5.18 풀이시간 10분 
T=int(input())
for tc in range(1,T+1):
    s=list(input())
    left=[]
    while len(s)>0:
        if s[0] in s[1:]:
            ri=s.index(s[0],1)
            del s[ri]
            del s[0]
        else:
            left.append(s[0])
            del s[0]
    ans="".join(sorted(left))
    if ans=="":
        ans="Good"
    print(f"#{tc} {ans}")