# 100만 이하의 모든 소수
import math
def prime_check(n):
    if n == 1 :
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    return True
for i in range(1,1000000):
  if prime_check(i):
    print(i,end=" ")