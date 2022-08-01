# 방법1 : 순회해서 풀기
# startswith 함수가 유용하게 쓰일 수 있음.
# str.startswith(str2) : str가 str2로 시작하면 True, 그렇지 않으면 False

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
        if phone_book[i].startswith(phone_book[i+1]):
            answer = False
            break
            
    return answer
  
# 방법2 : 해쉬
# 전화번호 목록을 해쉬맵으로 만듦
# 순회 -> 만약 접두어가 해쉬맵에 존재하면 False 리턴

def solution(phone_book):
    answer = True
    hashmap = {}
    for value in phone_book:
        hashmap[value] = 1

    for value in phone_book:
        temp = ""
        for num in value:
            temp += num
            
            if temp in hashmap and temp != value:
                return False
            
    return answer
