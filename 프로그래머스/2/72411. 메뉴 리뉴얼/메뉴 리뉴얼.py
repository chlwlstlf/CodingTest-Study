from itertools import combinations

def solution(orders, course):
    dict = {}
    for i in range(len(orders)):
        for j in range(len(course)):
            com = list(combinations(orders[i], course[j]))
            for c in com:
                c = ''.join(sorted(c)) # 오름차순 정렬하기
                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1
    # 코스 종류 별로 나누기
    cnt_list = [[] for _ in range(course[-1]+1)]
    for key, value in dict.items():
        if value >= 2:
            cnt_list[len(key)].append((key, value))
    
    # 코스 종류에서 가장 빈도가 많은 것 출력
    answer = []
    for cnt in cnt_list:
        if cnt:
            max_value = max(cnt, key=lambda item: item[1])[1]
            for j in range(len(cnt)):
                if cnt[j][1] == max_value:
                    answer.append(cnt[j][0])
    answer.sort()
    return answer