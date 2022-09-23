def solution(genres, plays):
    answer = []
    a = dict()
    k = dict()
    
    for i in range(len(genres)):
        a[genres[i]] = a.get(genres[i], 0) + plays[i]
        
        if genres[i] not in k :
            k[genres[i]] = [(i, plays[i])]
        else:
            k[genres[i]].append((i, plays[i]))
    
    b = []
    for i in a:
        b.append((i, a[i]))
    
    b.sort(key = lambda x: x[1], reverse=True)
    
    for i, v in b:
        value = k[i]
        value.sort(key = lambda x: x[1], reverse=True)
        for index, play_value in value[:2]:
            answer.append(index)
        
    
    return answer
