import sys
input = sys.stdin.readline

T = int(input())
coin = [25, 10, 5, 1]

for test_case in range(T):
    C = int(input())
    answer = []
    for i in range(4):
        answer.append(C//coin[i])
        C %= coin[i]
    print(*answer)