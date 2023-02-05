def solution(arr):
    answer = []
    n = 10
    for i in range(len(arr)):
        if n != arr[i]:
            answer.append(arr[i])
            n = arr[i] 
    return answer