# 1. 녹색 옷 입은 애가 젤다지? (골4)

'''
다익스트라
1. 순차 탐색: 거리 테이블을 매번 탐색하는 방식
2. 우선순위 큐: 거리가 짧은 노드를 우선 탐색
'''

import sys
import heapq
input = sys.stdin.readline

#다익스트라(우선순위 큐)
def dijkstra(cost, x, y):
  h = []
  heapq.heappush(h, (cost, x, y))
  while h:
    cost, x, y = heapq.heappop(h)
    if x == N-1 and y == N-1:
      return cost
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        heapq.heappush(h, (cost+C[nx][ny], nx, ny))


# 다익스트라 호출
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = 0
while True:
  N = int(input())
  t += 1
  if N == 0:
    break
  C = [list(map(int, input().split())) for _ in range(N)]
  visited = [[0 for _ in range(N)] for _ in range(N)]
  result = dijkstra(C[0][0], 0, 0)
  print("Problem %d: %d" %(t, result))


'''
print(h, cost) 출력 결과
[(5, 0, 0)] 5
[(8, 1, 0), (10, 0, 1)] 5
[(10, 0, 1), (11, 2, 0), (13, 0, 0), (17, 1, 1)] 8
[(11, 2, 0), (14, 0, 2), (13, 0, 0), (17, 1, 1)] 10
[(13, 0, 0), (13, 2, 1), (17, 1, 1), (14, 0, 2)] 11
[(13, 2, 1), (14, 0, 2), (17, 1, 1)] 13
[(14, 0, 2), (17, 1, 1), (20, 2, 2)] 13
[(15, 1, 2), (20, 2, 2), (17, 1, 1)] 14
[(17, 1, 1), (20, 2, 2)] 15
[(20, 2, 2)] 17
'''