### 아래서 부터 찾아 올라감
### 위쪽은 맨 마지막에 생각하고 왼쪽 아니면 오른쪽을 생각함

import sys
sys.stdin = open("input.txt")

for T in range(1,11):
    N = int(input())
    mat = []
    for i in range(100):
        mat.append(list(map(int,input().split())))
    for i in range(100):
        if mat[-1][i] == 2:
            end = i                     # 맨 아래쪽에 2가 있는 부분을 찾음
            break


    dx = [0, 0, -1]                     # 위쪽은 하나만
    dy = [1,-1, 0]                      # 오른쪽 왼쪽을 생각
    x = 99                              # 맨 밑부터 시작해서
    y = end                             # 시작함
    while x != 0:                       # x가 0이 될때까지
        for j in range(3):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<= nx < 100 and 0 <= ny < 100:              # 다음 가야 되는 x와 y가 0과 100 사이이면
                if mat[nx][ny]:                             # 그리고 mat[nx][ny] 가 0이아니면
                    x = nx
                    y = ny                                  # 다음 위치로 설정해줌
                    mat[nx][ny] = 0                         # 도착한 자리는 왔다감이라 표시해줌            
    print(f'#{T}', y)   



