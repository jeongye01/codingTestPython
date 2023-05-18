#럭키 스트레이트
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")




'''
#내풀이 -> 테스트 통과  DATE->4.12 풀이시간->7분
n=input()

half=len(n)//2
sum=0
for x in n[0:half]:
  sum+=int(x)


for x in n[half:]:
  sum-=int(x)


if(sum==0):
  print("LUCKY")
else:
  print("READY")


'''



'''
#내풀이 -> 테스트 통과  DATE->5.18 풀이시간->5분
n=list(map(int,str(input())))
if sum(n[0:len(n)//2])==sum(n[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")


'''