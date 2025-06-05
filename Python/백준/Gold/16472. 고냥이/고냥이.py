# 고냥이 (골4)

import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()

start = 0
end = 0
answer = 0
visited = [0]*26
visited[ord(s[0]) - ord("a")] = 1
cnt = 1

while start < len(s) and end < len(s):
  if cnt <= N:
    answer = max(answer, end-start+1)
    end += 1
    if end < len(s):
      visited[ord(s[end]) - ord("a")] += 1
      if visited[ord(s[end]) - ord("a")] == 1:
        cnt += 1
  else:
    visited[ord(s[start]) - ord("a")] -= 1
    if visited[ord(s[start]) - ord("a")] == 0:
      cnt -= 1
    start += 1
    
print(answer)