# sort(기준, reverse)
# '구분자',join(리스트) -> 문자열
def solution(numbers):
    answer = ''
    arr = list(map(str, numbers))
    arr.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(arr)))
    return answer
