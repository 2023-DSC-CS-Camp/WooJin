from collections import deque

# 미로 입력 받기
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 시작점과 도착점 설정
start = (1, 1)
end = (n, m)

# 방문한 적이 있는 칸 체크를 위한 visited 배열 초기화
visited = [[False] * (m+1) for _ in range(n+1)]

# 시작점부터 해당 칸까지의 거리를 저장하기 위한 distance 배열 초기화
distance = [[0] * (m+1) for _ in range(n+1)]

# BFS 알고리즘 구현
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque([start])
visited[start[0]][start[1]] = True

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로의 범위를 벗어나는 경우 무시
        if nx < 1 or nx > n or ny < 1 or ny > m:
            continue
        # 벽인 경우 무시
        if maze[nx-1][ny-1] == 0:
            continue
        # 이미 방문한 적이 있는 경우 무시
        if visited[nx][ny]:
            continue
        queue.append((nx, ny))
        visited[nx][ny] = True
        distance[nx][ny] = distance[x][y] + 1

# 도착점까지의 최단 거리 출력
print(distance[end[0]][end[1]] + 1)