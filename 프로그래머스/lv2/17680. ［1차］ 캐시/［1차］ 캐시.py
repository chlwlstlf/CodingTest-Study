from collections import deque

def solution(cacheSize, cities):
    answer = 0

    cities = [i.lower() for i in cities]
    q = deque()
    for i in range(len(cities)):
        if cities[i] in q:
            q.remove(cities[i])
            q.appendleft(cities[i])
            answer += 1
        else:
            q.appendleft(cities[i])
            if len(q) > cacheSize:
                q.pop()
            answer += 5
    
    return answer