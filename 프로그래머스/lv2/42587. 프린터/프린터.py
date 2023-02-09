def solution(priorities, location):
    result = [i for i in range(len(priorities))]
    priorities2 = []
    result2 = []
    while True:
        if priorities[0] != max(priorities):
            priorities.append(priorities.pop(0))
            result.append(result.pop(0))
        else:
            priorities2.append(priorities.pop(0))
            result2.append(result.pop(0))

        if len(priorities) == 0:
            break
            
    answer = result2.index(location)+1
    return answer