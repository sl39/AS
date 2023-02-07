# 총 4가지 경우이다
# 첫번쨰는 오른쪽으로 가는 경우
# 두번째는 아래로 가는 경우
# 세번째는 왼쪽으로 가는 경우
# 네번째는 위로 가는 경우
# 이렇게 총 4가지 경우가 있고
# 첫번째 경우에서는 오른쪽으로 쭉 가다가 범위를 벗어나거나 이미 값이 저장되어 있으면 멈추고 다음 작업으로 넘어간다
# 두번째 경우에서도 마찬가지로 아래로 쭉 가다가 범위를 벗어나거나 이미 값이 저장되어 있으면 다음 작업으로 넘어간다
# 세번째 , 네번째도 마찬가지로 하고
# 네번째 작업이 끝나고 오른쪽으로 가는 길이 있으면 다시 이 4작업을 반복 한다
# 그리고 더 이상 갈 길이 없으면 종료, 리스트를 출력한다


TC = int(input())
for T in range(1,TC+1):
    N = int(input())
    
    if N == 1:                          # N = 1 일 경우 그냥 1 을 출력
        print(f"#{T}")
        print(1)
        
    else:                                       # 아닐 경우
        new_mat = [[0]*N for j in range(N)]         # 먼저 출력할 행렬을 만들고
        new_list = list(range(1,N*N+1))             # 들어갈 리스트들을 생성한다
        x= 0
        y= 0
        new_mat[0][0] = new_list[0]                 # 행렬의 맨 왼쪽 위는 리스트의 첫번째 수를 저장하고 시작한다
        t = 1
        while new_mat[x][y+1] == 0:             # 오른쪽, 아래, 왼쪽, 위 작업이 끝나고 다시 오른쪽 작업이 없을 경우 종료
            
            # 이 경우는 오른쪽으로 계속 가다가 더 이상 갈 곳이 없으면 종료
            while not new_mat[x][y+1]:
                y = y+1
                new_mat[x][y] = new_list[t]             # 리스트에서 t 번째 리스트를 저장ㄴ
                t = t+1
                if y+1 < N:
                    pass
                else:
                    break
            
            
            # 이 경우는 아래로 가다가 더 이상 갈 곳이 없으면 종료
            while not new_mat[x+1][y]:      
                x = x + 1
                new_mat[x][y] = new_list[t]
                t = t + 1
                if x + 1 <N:
                    pass
                else:
                    break

                    
            # 이 경우는 왼쪽으로 가다가 더 이상 갈 곳이 없으면 종료
            while not new_mat[x][y-1]:
                y = y - 1
                new_mat[x][y] = new_list[t]
                t = t + 1
                if y-1 >= 0:
                    pass
                else:
                    break
            # 이경우는 위로 가다가 더 이상 갈 곳이 없으면 종료
            
            while not new_mat[x-1][y]:
                x = x - 1
                new_mat[x][y] = new_list[t]
                t = t + 1
                if x - 1>= 0:
                    pass
                else:
                    break
        # 그리고 결과 값을 종료
        print(f"#{T}")
        for i in new_mat:
            print(*i)