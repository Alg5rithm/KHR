def solution(cacheSize, cities):
    answer = 0
    
    maps = {}
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city not in maps:
            answer += 5
            
            if len(maps) != cacheSize:
                maps[city] = 1
            else:
                max_val = max(maps.values())
                for key in maps.keys():
                    if max_val == maps[key]:
                        del maps[key]
                        maps[city] = 1
                        break
        else:
            answer += 1
            maps[city] = 1
            
        for key in maps.keys():
            if key != city:
                maps[key] = maps[key] + 1  
            
    return answer
