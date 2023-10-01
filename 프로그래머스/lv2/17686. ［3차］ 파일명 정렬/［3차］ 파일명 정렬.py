def solution(files):
    # HEAD, NUMBER로 쪼개기
    arr = []
    for i in range(len(files)):
        a = [i]
        for j in range(len(files[i])):
            if files[i][j] >= '0' and files[i][j] <= '9':
                a.append(files[i][0:j].lower())
                idx = j
                break
        for j in range(idx, len(files[i])):
            if not (files[i][j] >= '0' and files[i][j] <= '9'):
                a.append(int(files[i][idx:j]))
                break
            if j == len(files[i])-1:
                a.append(int(files[i][idx:]))
        arr.append(a)
    # 순서대로 출력하기
    arr.sort(key=lambda x:(x[1], x[2], x[0]))
    answer = []
    for i in range(len(arr)):
        answer.append(files[arr[i][0]])
    return answer