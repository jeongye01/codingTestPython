#민정이와 광직이의 알파벳 공부
#내 풀이->테스트 통과 DATE=>5.21 풀이시간 30분 
from itertools import combinations
T=int(input())

def check(chars):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for x in chars:
        if x in alpha:

            del alpha[alpha.index(x)]


    if len(alpha)==0:
        return True
    else:
        return False


for tc in range(1,T+1):
    n=int(input())
    words=[]
    for _ in range(n):
        words.append(input())

    ans=0
    for i in range(1,n+1):
        comb=list(combinations(words,i))

        for c in comb:
            tmp = set()
            for i in c:
                for j in i:
                    tmp.add(j)

            if check(list(tmp)):
                #print(tmp)
                ans+=1





    print(f"#{tc} {ans}")