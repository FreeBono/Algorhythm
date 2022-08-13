```python
import sys
sys.stdin=open('input.txt')


def dfs(depth):
    global cnt
    if depth == n:
        cnt += 1
        return
    for i in range(n):
        if visited[i] == 0:
            graph[depth] = i
            
            flag = True
            for j in range(depth):
                if abs(graph[depth] - graph[j]) == abs(depth-j):
                    flag = False
                    break
            
            if flag:
                
                visited[i] = 1
                dfs(depth + 1)
                visited[i] = 0


n = int(input())
graph = [0]*n
visited = [0]*n

cnt = 0
dfs(0)
print(cnt)
```

