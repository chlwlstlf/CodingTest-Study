from collections import deque

def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    boardT = []
    for j in range(n):
        t = deque()
        for i in range(m):
            t.append(board[i][j])
        boardT.append(t)

    answer = 0
    while True:
        # 2x2 찾기
        result = set()
        for i in range(n-1):
            for j in range(m-1):
                if boardT[i][j] != 0:
                    if boardT[i][j] == boardT[i][j+1] and boardT[i][j] == boardT[i+1][j] and boardT[i][j] == boardT[i+1][j+1]:
                        result.add((i, j))
                        result.add((i, j+1))
                        result.add((i+1, j))
                        result.add((i+1, j+1))
        if not result:
            break
        answer += len(result)
            
        # 블록 지우고 내리기
        for r in result:
            boardT[r[0]][r[1]] = 0
        for i in range(n):
            if 0 in boardT[i] :
                for j in range(m):
                    if boardT[i][j] == 0:
                        del boardT[i][j]
                        boardT[i].appendleft(0)
    return answer