def solution(people, limit):
    answer = 0
    people.sort()
    idx = len(people) - 1
    i = 0
    while i <= idx:
        answer += 1
        if people[i] + people[idx] <= limit:
            i += 1
        idx -= 1

    return answer
