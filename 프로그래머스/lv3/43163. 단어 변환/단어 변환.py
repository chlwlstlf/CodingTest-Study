from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0]*len(words)
    
    #변환할 수 없을 때 예외 처리
    if target not in words:
        return 0
    
    def bfs(word):
        nonlocal answer
        q = deque()
        q.append(word)
        while q :
            word = q.popleft()
            for i in range(len(words)):
                cnt = 0
                for j in range(len(words[i])):
                    if word[j] == words[i][j]:
                        cnt += 1
                if cnt == len(word)-1 and visited[i] == 0:
                    if word == begin:
                        visited[i] = 1
                    else:
                        visited[i] = visited[words.index(word)]+1
                    q.append(words[i])      
            if visited[words.index(target)] != 0:
                return visited[words.index(target)]
    
    return bfs(begin)