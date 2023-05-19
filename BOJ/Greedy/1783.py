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