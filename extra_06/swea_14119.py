def check(cnt,depth):
    global ans
    if depth == 12:
        ans = min(ans,cnt)
        return
    
    if ans < cnt:
        return
    
    check(cnt+arr[depth]*day,depth+1)
    check(cnt+month,depth+1)
    if depth <= 9:
        check(cnt+m3,depth+3)


TC = int(input())

for T in range(1,TC+1):
    day, month, m3, year = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = year
    check(0,0)
    print(f'#{T}', end=" ")
    print(ans)