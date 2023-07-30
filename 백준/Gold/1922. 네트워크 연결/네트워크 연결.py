# 1. 네트워크 연결 (골4)

# 1. 프림 알고리즘
# 1) 임의의 정점을 시작 정점으로
# 2) 최소 신장 트리의 루트 노드로 삽입
# 3) 삽입된 정점과 인접한 정점의 가중치 비교

# 2. 크루스칼 알고리즘
# 1) 가중치의 오름차순 정렬
# 2) 사이클 간선 제외
# 3) MST 집합에 추가

import sys
import heapq
input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())
h = []
for i in range(M):
  l = list(map(int, input().split()))
  heapq.heappush(h, (l[2], l[0], l[1]))

# find 함수
def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

# 크루스칼
parent = [i for i in range(N+1)]
result = 0
for i in range(M):
  c, a, b = heapq.heappop(h)
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

  if a != b:
    result += c

print(result)