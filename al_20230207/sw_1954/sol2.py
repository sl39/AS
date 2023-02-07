def make_graph(n):
    # 번호를 저장해서 반환할 배열
    graph = [[0] * n for _ in range(n)]

    # 시작 위치
    x, y = 0, -1

    # 함수 내에서 사용할 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0

    for i in range(n ** 2 - 1, 0, -1):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 벽을 만나거나 값이 채워진 위치에서 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 0:
            dir = (dir + 1) % 4

            nx = x + dx[dir]
            ny = y + dy[dir]

        graph[nx][ny] = i
        x, y = nx, ny

    return graph

arr = make_graph(5)

for i in arr:
    print(i)