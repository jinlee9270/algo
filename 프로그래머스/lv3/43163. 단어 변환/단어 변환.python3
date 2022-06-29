def solution(begin, target, words):
    answer = 0
    words.append(begin)
    word_n= len(words)
    word_num = len(words[0]) 
    edges = [[] for _ in range(word_n)]
    visited = [float('inf')] * word_n
    
    if target not in words:
        return answer
    
    else:
        tar_idx = words.index(target)
        for i in range(word_n):
            for j in range(i+1, word_n):
                cnt = 0
                for k in range(word_num):
                    if words[i][k] == words[j][k]:
                        cnt += 1
                if cnt == word_num - 1:
                    edges[j].append(i)
                    edges[i].append(j)
        
        #bfs 부분
        q = [word_n - 1]
        visited[word_n - 1] = 0
        while len(q) > 0:
            cur = q.pop(0)
            
            for nxt in edges[cur]:
                if visited[nxt] > visited[cur] + 1:
                    visited[nxt] = visited[cur] + 1
                    q.append(nxt)
                    
        print(visited, edges)
        if visited[tar_idx] != float('inf'):
            return visited[tar_idx]
        else:
            return 0