###내 풀이->테스트 통과 DATE=>5.13 풀이시간 60분 
def caesarCipher(s, k):
    # Write your code here
    news=""
    d1=ord('z')-ord('a')+1
    d2=ord('Z')-ord('A')+1
    #print(chr((ord("f")+98-ord('z'))%d1))
    for x in s:
        if ord('a')<=ord(x)<=ord('z'):
            res=ord(x)+k
            if res>ord('z'):
              tmp=abs(res-ord('z'))%d1
              if tmp==0:
                res=ord('z')
              else:
                res=tmp+ord('a')-1
            news+=chr(res)
        elif ord('A')<=ord(x)<=ord('Z'):
            res=ord(x)+k
            if res>ord('Z'):
              tmp=abs(res-ord('Z'))%d2
              if tmp==0:
                res=ord('Z')
              else:
                res=tmp+ord('A')-1
            news+=chr(res)
        else:
            news+=x

'''
# 더 나은 풀이
def caesarCipher(s, k):
    
    result = list(map(lambda x : chr((ord(x)-ord('a')+k)%26+ord('a')) if x.islower() else x, s))
    result = list(map(lambda x : chr((ord(x)-ord('A')+k)%26+ord('A')) if x.isupper() else x, result))

    return ''.join(result)

'''