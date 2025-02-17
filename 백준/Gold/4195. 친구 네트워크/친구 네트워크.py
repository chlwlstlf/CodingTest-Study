# 친구 네트워크 (골2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(v):
  if parent[v] < 0:
    return v
  parent[v] = find(parent[v])
  return parent[v]

T = int(input())
for _ in range(T):
  F = int(input())
  name = {}
  parent = [-1]*(F*2+1)
  for _ in range(F):
    a, b = input().rstrip().split(" ")
    if a not in name:
      name[a] = len(name)+1
    if b not in name:
      name[b] = len(name)+1
    parentA = find(name[a])
    parentB = find(name[b])
    if parentA != parentB:
      parent[parentB] += parent[parentA]
      parent[parentA] = parentB
    print(-parent[parentB])