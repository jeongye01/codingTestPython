#https://www.acmicpc.net/problem/1783
#병든나이트
##내 풀이->테스트 통과 DATE=>5.19 풀이시간 60분 
import math
n,m=map(int,input().split()) #n세로 m 가로

if n==1 or m==1:
    ans=1
elif n==2:
    if m<=7:
        ans=math.ceil(m/2)
    else:
        ans=4
else:
    if m==2:
        ans=2
    elif m==3:
        ans=3
    elif m < 7:
        ans = 4
    else:
        ans=3+(m-5)
print(ans)

'''
min으로 코드 단축시키기
N, M = map(int, input().split())
if N == 1:
    scount = 1
elif N == 2:
    scount = min(4, (M-1)//2 + 1)
elif M < 7:
    scount = min(4, M)
else:
    scount = (2 + (M-5)) + 1
print(scount)



'''