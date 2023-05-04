#간단한 압축 풀기
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 7분 
T = int(input())
for tc in range(1, T + 1):
  n=int(input())
  array=[]
  for i in range(n):
    c,cn=input().split()
    array.append((c,int(cn)))
  tmp=""
  result=[]
  for i in range(n):
    tmp+=array[i][0]*array[i][1]
    while len(tmp)>10:
      result.append(tmp[0:10])
      tmp=tmp[10:]
  result.append(tmp) 
  print("#{}".format(tc))
  for a in result:
    print(a)