import sys
sys.stdin = open('sample_input.txt')

def BT(start):
    stack = [start]
    while stack:
        start = stack.pop()
        for k in range(4):
            nx, ny = dx[k] + start[1], dy[k] + start[0]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == 3:
                    return 1
                if arr[ny][nx] == 0:
                    stack.append([ny, nx])
                    arr[ny][nx] += 1
    return 0

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                break
    print(f'#{tc}', BT(start))