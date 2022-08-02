import math

def get_width_height(square):
    array = []
    number = int(math.sqrt(square))
    for i in range(square, number, -1):
        if square % i == 0:
            array.append((i, square//i))
    if number * number == square :
        array.append((number, number))
    return array

def solution(brown, yellow):
    answer = []
    square = brown + yellow
    arr = get_width_height(square)
    arr2 = get_width_height(yellow)
    
    for val in arr:
        x, y = val
        w = 2 * (x+y)
        
        # 노란색 부분은 w-2, h-2임. 해당 width와 heigth로 면적이 yellow라면 
        yx, yy = x-2, y-2
        if yx * yy == yellow:
            answer = [x,y]
            break

    return answer
