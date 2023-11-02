import re
import copy
from itertools import permutations

def solution(expression):
    operator = ['+', '-', '*']
    expression = re.findall(r'\d+|[+\-\*]', expression)
    # 우선순위 바꿔가며 계산하기
    answer = 0
    permutation = list(permutations(operator, 3))
    for perm in permutation:
        exp = copy.deepcopy(expression)
        for p in perm:
            j = 0
            while j < len(exp):
                if exp[j] == p:
                    a, b = int(exp[j-1]), int(exp[j+1])
                    if p == '+': exp[j] = a + b
                    if p == '-': exp[j] = a - b
                    if p == '*': exp[j] = a * b
                    del exp[j + 1]
                    del exp[j - 1]
                else:
                    j += 1
        if abs(exp[0]) > answer:
            answer = abs(exp[0])
    return answer