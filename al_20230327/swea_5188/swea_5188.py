TC = int(input())

dx = [1,0]
dy = [0,1]

def find(res,start):
    global mx
    if mx < res:
        return
    if start == (n-1,n-1):
        mx = min(mx,res)
        return
    x,y = start
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and ny < n:
            find(res+mat[nx][ny],(nx,ny))
        
for T in range(1,TC+1):
    mat = []
    mx = 500
    n = int(input())
    for i in range(n):
        mat.append(list(map(int,input().split())))
    
    find(mat[0][0],(0,0))
    print(f"#{T}", mx)
    
    