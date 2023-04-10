'''
# 내풀이
s=input()

result=int(s[0])

one_ctn=0
zero_ctn=0
focus=-1
for x in s:
  if (focus!=x):
    focus=x
    if(int(x)==1):one_ctn+=1
    else: zero_ctn+=1
  

print(min(zero_ctn,one_ctn))
'''