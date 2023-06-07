#https://school.programmers.co.kr/learn/courses/30/lessons/42577
##내 풀이->테스트 통과 DATE=>6.5 풀이시간 15분 
def solution(phone_book):
    phone_book.sort()
    #head={}
    for i in range(1,len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False
        
    
    return True