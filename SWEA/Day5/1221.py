# [S/W 문제해결 기본] 5일차 - GNS
#내 풀이->테스트 통과 DATE=>5.5 풀이시간 12분 
T = int(input())
nmap={
  "ZRO":0,
  "ONE":1,
  "TWO":2,
  "THR":3,
  "FOR":4, 
  "FIV":5,
  "SIX":6,
  "SVN":7, 
  "EGT":8, 
  "NIN":9
}

for tc in range(1, T + 1):
  dummy,n=input().split()
  n=int(n)
  data=list(input().split())
  data.sort(key=nmap.get)
  print(f"#{tc}\n", *data)