# 3. 최소 스패닝 트리 (골4)

# 크루스칼
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
h = []
for i in range(E):
  A, B, C = map(int, input().split())
  heappush(h, (C, A, B))

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]


parent = [i for i in range(V+1)]
result = 0
for i in range(E):
  c, a, b = heappop(h)
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  if a != b:
    result += c

print(result)