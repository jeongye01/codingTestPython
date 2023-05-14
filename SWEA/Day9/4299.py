#태혁이의 사랑은 타이밍
#내 풀이->테스트 통과 DATE=>5.14 풀이시간 12분 
# 약속시간 전, h는 일치하는 경우,오늘인경우,오늘이후인 경우 케이스 분리함
T=int(input())
for tc in range(1,T+1):
    d,h,m=map(int,input().split())
    ans=0 #분 단위
    if d==11:
        if h<11 or (h==11 and m<11): #약속시간전
            ans=-1
        elif h==11:
            ans=h-11
        else:
            ans=(h-12)*60+49+m
    else:
        ans=(d-12)*24*60+h*60+m+12*60+49



    print(f"#{tc} {ans}")