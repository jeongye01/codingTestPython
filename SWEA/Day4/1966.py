#숫자를 정렬하자
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 2분 
T = int(input())
for test_case in range(1, T + 1):
  n=int(input())
  array=list(map(int,input().split()))
  array.sort()
  print("#{}".format(test_case),end=" ")
  for a in array:
    print(a,end=" ")
  print()