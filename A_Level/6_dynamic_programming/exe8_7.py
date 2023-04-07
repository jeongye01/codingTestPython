# 정수 N을 입력받기
n = int(input())


# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i-1]+2*d[i-2])%796796

# 계산된 결과 출력
print(d[n])

'''
#내 풀이->top down
n=int(input()) #가로 길이

result=0 # 바닥을 채우는 경우의 수 


d=[0]*1000

def get_case(x):
  if(x==2): return 3
  elif(x==1): return 1
  else:
    if(d[x]!=0):
      return d[x]
    d[x]=get_case(x-1)+2*get_case(x-2)
    return d[x]

  
print(get_case(n)%796796)

'''