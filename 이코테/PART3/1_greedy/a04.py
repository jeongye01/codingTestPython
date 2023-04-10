n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
# 만들 수 없는 금액 출력
print(target)

'''
from itertools import combinations
n=int(input())
array=list(map(int,input().split()))

array.sort()

result=0
sum_set=set()
for i in range(1,n+1):
  comb=combinations(array,i)
  for c in comb:
    sum_set.add(sum(c))


result=min(sum_set)
for integer in sum_set:
  if(result!=integer):
    break
  result+=1

print(result)
  '''