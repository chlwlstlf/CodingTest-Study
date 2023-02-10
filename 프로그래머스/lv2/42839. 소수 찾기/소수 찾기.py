from itertools import permutations

def solution(numbers):
    answer = 0
    arr = []
    numbers = list(map(int, numbers))
    
    #조합가능한 숫자들 구하기
    for i in range(len(numbers)):
        per = list(permutations(numbers, i+1))
        for p in per:
            arr.append(int(''.join(map(str, p))))
    arr = list(set(arr))

    #소수찾기
    for i in range(len(arr)):
        f = 0
        for j in range(2, arr[i]):
            if arr[i]%j == 0:
                f = 1
                break
        if f == 0 and arr[i] > 1:
            answer +=1
                       
    return answer