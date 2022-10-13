def solution(n, words):
    answer = []
    
    result = 1
    index = 2
    flag = True
    word_set = set()
    prev_word = words[0]
    word_set.add(prev_word)
    for i in range(1, len(words)):
        word = words[i]
        if word in word_set:
            answer.append(index)
            flag = False
            break
        if prev_word[len(prev_word)-1] != word[0]:
            answer.append(index)
            flag = False
            break
        index += 1
        if index > n :
            result += 1
            index = 1
        prev_word = word
        word_set.add(word)
    
    if flag:
        return [0,0]
    answer.append(result)
    return answer
