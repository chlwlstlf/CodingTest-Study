def solution(sizes):
    r_max = 0
    c_max = 0
    for i in range (len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][0] > r_max:
            r_max = sizes[i][0]
        if sizes[i][1] > c_max:
            c_max = sizes[i][1]
    return r_max*c_max