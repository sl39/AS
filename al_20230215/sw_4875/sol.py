import sys
sys.stdin = open("sample_input.txt")


def dfs(v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    global mat
    stack = [v]                                 # 시작점이 v이므로
    while stack:                                # 스택이 빌때까지 while문을 돌림
        p = stack.pop()
        for i in range(4):                      # 델타 탐색 으로 상하좌우 검색
            nx = dx[i] + p[0]
            ny = dy[i] + p[1]
            if 0 <= nx < n and 0 <= ny < n:     # out of range 피하기위한 if 문
                if mat[nx][ny] == "3":              # 만약 3을 찾았다면 1을 리턴하고 함수를 종료
                    return 1
                elif mat[nx][ny] == "0":        # 아니면 mat[nx][ny] 가 0 이면 길이 있다는 이야기므로
                    stack.append([nx, ny])      # [nx, ny] 이쪽으로 갔다고 생각하고 스택에 넣는다
                    mat[nx][ny] = "1"           # 그리고 지나간 길이므로 1으로 바꿔줌
                                                # 스택이 비었는데, 즉 갈수 있는 모든 길을 탐색했는데 함수가 종료가 되지 않았으면
    return 0                                    # 0을 반환해준다




TC = int(input())
for T in range(1,TC+1):
    n = int(input())

    mat = []
    for i in range(n):
        mat.append(list(input().strip()))
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "2":            # 2를 찾는 [i,j]
                v = [i, j]
                break

    print(f"#{T}",dfs(v))


