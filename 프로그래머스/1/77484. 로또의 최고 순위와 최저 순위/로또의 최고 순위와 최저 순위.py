def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [0, 0]
    for l in lottos:
        if l == 0:
            answer[0] += 1
        else:
            if l in win_nums:
                answer[0] += 1
                answer[1] += 1
    answer = [rank[answer[i]] for i in range(2)]
    return answer