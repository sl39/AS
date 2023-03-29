TC = int(input())


def comb(res,depth):
    global mx
    if depth == n:
        if res>= b:
            mx = min(mx,res)
        return
    
    if res > mx:
        return
    
    comb(res+arr[depth],depth+1)
    comb(res,depth+1)

for T in range(1,TC+1):
    n,b = map(int,input().split())
    arr = list(map(int,input().split()))
    mx = n*b
    comb(0,0)
    print(f'#{T}',end=" ")
    print(mx-b)