#캠핑
#https://www.acmicpc.net/problem/4796
lpv=[]
while True:
  lpv.append(list(map(int,input().split())))
  if(lpv[-1]==[0,0,0]):
    lpv.pop()
    break
idx=0
for c in lpv:
  idx+=1
  l,p,v=c[0],c[1],c[2]
  ans=(v//p)*l+(l if v%p>=l else v%p)
  
    
  print(f"Case {idx}: {ans}")