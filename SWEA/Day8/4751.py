#다솔이의 다이아몬드 장식
##내 풀이->테스트 통과 DATE=>5.10 풀이시간 15분 
T = int(input())
for tc in range(1, T + 1):
  s = input()
  result = ["" for i in range(5)]
  last = [".", ".", "#", ".", "."]
  letter = [[
    ".",
    ".",
    "#",
    ".",
  ], [
    ".",
    "#",
    ".",
    "#",
  ], [
    "#",
    ".",
    "",
    ".",
  ], [
    ".",
    "#",
    ".",
    "#",
  ], [
    ".",
    ".",
    "#",
    ".",
  ]]
  for i in range(len(s)):
    for j in range(5):
      for k in range(4):
        if(letter[j][k]==""):
          result[j]+=s[i]
        else:
          result[j]+=letter[j][k]
  for i in range(5):
    result[i]+=last[i]
    
  for r in result:
    print(r)