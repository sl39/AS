TC =int(input())
    

def find(depth,cnt):
    global res
    
    if n == depth:
        print(arr)
        res = min(res,cnt)
        return
    
    for i in range(n):
        if i != depth:
            if arr[i] == n:
                arr[i] = depth
                find(depth+1, cnt+mat[depth][i])
                arr[i] = n

for T in range(1,TC+1):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    res = 5000
    arr = [n]* n
    find(0,0)
    print(res)
    
    
def check(arr):
    visited = [0] * n
    p = 0
    t = 0 
    while t <n:
        if not visited[p]:
            visited[p] = 1