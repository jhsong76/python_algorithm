from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [ -1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]

q = deque([(0, 0)])

visited[0][0] = 1

while q:
    x, y = q.popleft()
    
    if x == n - 1 and y == m - 1:
        print(visited[x][y])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))