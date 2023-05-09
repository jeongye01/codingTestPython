#최대 성적표 만들기
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 2분 
T = int(input())
for tc in range(1,T+1):
  n,k=map(int,input().split())
  array=list(map(int,input().split()))
  array.sort(reverse=True)
  
  print(f"#{tc}",sum(array[0:k]))