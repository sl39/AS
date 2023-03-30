TC = int(input())

def perm(depth):
    global mn, AA,BB
    if depth == n//2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if i !=j:
                    if arr[i] and arr[j]:
                        A += mat[i][j]
                    elif not arr[i] and not arr[j]:
                        B += mat[i][j]
        
        mn = min(mn,abs(A-B))
        return
    
    for i in range(n):
        if arr[i] == 0:
            arr[i] = 1
            perm(depth+1)
            arr[i] = 0


for T in range(1,TC+1):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    arr = [0] * n

    
    mn =AA=BB= 100000
    perm(0)
    print(f'#{T}',mn)