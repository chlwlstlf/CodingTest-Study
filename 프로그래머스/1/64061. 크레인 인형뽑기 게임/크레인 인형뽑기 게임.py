from collections import deque

def solution(board, moves):
    # 전치행렬로 바꾸기
    board_T = list(map(deque, zip(*board)))
    # 인형 뽑고 터트리기
    answer = 0
    result = []
    for m in moves:
        m -= 1
        for i in range(len(board_T[m])):
            if board_T[m][i] != 0:
                result.append(board_T[m][i])
                del board_T[m][i]
                board_T[m].appendleft(0)
                break
        if len(result) >=2 and result[-1] == result[-2]:
            result = result[:-2]
            answer += 2
    return answer