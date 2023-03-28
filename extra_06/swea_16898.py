TC= int(input())


def comb(res, i):
    global cnt
    if res == m:
        cnt += 1
        return
    
    if i == n:
        return
    
    comb(res+arr[i], i+1)
    comb(res, i+1)
    
for T in range(1,TC+1):
    n,m = map(int,input().split())
    arr =list(map(int,input().split()))
    cnt = 0
    comb(0, 0)
    print(f"#{T}", end=" ")
    print(cnt)