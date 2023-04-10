# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001
# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)

for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])


'''
내 풀이 -> 탑다운 방식
d=[0]*30001
n=int(input())
result=0
def makeOne(x):
  if(x==1): #x가 0이면 계산할 필요 없음 
    return 0
  else:
    if(d[x]!=0):return d[x]
    temp=[]
    
    if(x%5==0): #5로 나누어 떨어짐
      temp.append(makeOne(x//5))
    if(x%3==0): #3로 나누어 떨어짐
      temp.append(makeOne(x//3))
    if(x%2==0): #2로 나누어 떨어짐
      temp.append(makeOne(x//2))
    
    temp.append(makeOne(x-1))
    d[x]=min(temp)+1
    return d[x]
    


print(makeOne(n))
'''