#https://school.programmers.co.kr/learn/courses/30/lessons/155652
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 20분 
def solution(s, skip, index):
    answer = ''
    for x in s:
       cnt=0
       c=ord(x)
       while cnt!=index:
           c+=1
           if c>ord('z'):
               c=ord('a')
           if chr(c) not in skip:
               cnt+=1
       answer+=chr(c)
    return answer


'''

def solution(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    ans = ''
    for i in s:
        ans += atoz[(atoz.index(i)+index)%len(atoz)]

    return ans

'''