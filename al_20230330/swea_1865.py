TC = int(input())


def qqq(depth, res):
    global ans
    if depth == n:
        ans = max(ans,res)
        return
    
    if ans >= res:
        return
    
    for i in range(n):
        if not arr[i]:
            arr[i] = 1
            qqq(depth+1,res*(mat[depth][i]/100))
            arr[i] = 0
    

for T in range(1,TC+1):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    arr = [0] * n
    ans = 0
    # round(ans*100)
    qqq(0,1)
    print(f'#{T}', end=" ")
    ans = str(round(ans*100,6))
    a = len(ans)
    for i in range(a):
        if ans[i] == '.':
            idx = i
    ans = ans + '0'* (6-(a-idx)+1)
    
    print(ans)