def solution(record):
    # 문자열 끊어서 배열로 만들기
    arr = [list(map(str, record[i].split())) for i in range(len(record))]
    # 최종 닉네임
    dict = {}
    for i in range(len(record)):
        if arr[i][0] != 'Leave':  
            dict[arr[i][1]] = arr[i][2]
    # 출력
    answer = []
    for i in range(len(record)):
        if arr[i][0] == 'Enter':
            answer.append(dict[arr[i][1]] + "님이 들어왔습니다.")
        if arr[i][0] == 'Leave':
            answer.append(dict[arr[i][1]] + "님이 나갔습니다.")
    return answer