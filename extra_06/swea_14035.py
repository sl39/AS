TC = int(input())

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def dfs(res,depth,x,y):
    if depth == 6:
        if not (res,depth,x,y) in dic:
            dic[(res,depth,x,y)] = 0
            arr.append(int(res))
        
            return
    
    if (res,depth,x,y) in dic:
        return
    dic[(res,depth,x,y)] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < 4 and 0<= ny < 4:
            dfs(res+mat[nx][ny],depth+1,nx,ny)
    
    



for T in range(1,TC+1):
    mat = []
    for i in range(4):
        mat.append(list(map(str,input().split())))
    dic = {}
    arr = []
    for i in range(4):
        for j in range(4):
            dfs(mat[i][j],0,i,j)
    print(f"#{T}", end=" ")
    print(len(set(arr)))