
def perm(depth,res):
    global ans
    if depth == n:
        ans = min(ans,res)
        return
    
    if res > ans:
        return
    
    for i in range(n):
        if arr[i] ==0:
            arr[i] = 1
            perm(depth+1,res+ mat[depth][i])
            arr[i] = 0
            


TC = int(input())

for T in range(1,TC+1):
    n = int(input())
    mat= [list(map(int,input().split())) for i in range(n)] 
    ans = 1500
    arr = [0] * n
    perm(0,0)
    print(f'#{T}', end=" ")
    print(ans)