import math

def solution(fees, records):
    answer = []
    dict1 = {}
    dict2 = {}
    # records 돌면서 시간 dict2에 넣어주기
    for r in records:
        time = int(r[0:2])*60 + int(r[3:5])
        if r[11:] == 'IN':
            dict1[r[6:10]] = time
        else:
            if r[6:10] in dict2:
                dict2[r[6:10]] += time - dict1[r[6:10]]
            else:
                dict2[r[6:10]] = time - dict1[r[6:10]]
            dict1.pop(r[6:10])
                
    # 출차 내역 없는 차도 계산해주기
    time = 23*60 + 59
    for key in dict1:
        if key in dict2:
            dict2[key] += time - dict1[key]
        else:
            dict2[key] = time - dict1[key]
    # 계산 해주기
    dict2 = dict(sorted(dict2.items()))
    for key in dict2:
        if dict2[key] <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil((dict2[key] - fees[0])/fees[2])*fees[3]
            answer.append(fee)
    return answer