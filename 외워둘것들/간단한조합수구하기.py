import math
def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
T = int(input())

for tc in range(1, T + 1):
  n,r=map(int,input().split())
  ans=nCr(n,r)
  print(f"#{tc} {ans}")
  