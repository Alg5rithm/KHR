s = input()

a = s.split("0")
b = s.split("1")
count_a = 0
count_b = 0
if len(a) == 1 or len(b) == 1 :
    print(0)
else :
    for val in a :
        if val != '' :
            count_a += 1
    
    for val in b :
        if val != '' :
            count_b += 1

    print(min(count_a,count_b))
