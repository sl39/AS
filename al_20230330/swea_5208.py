TC = int(input())


def perm(depth,res):
    global cnt
    if depth >= n-1:
        cnt = min(cnt,res)
        return 
    if res >= cnt:
        return
    
    
    
    for i in range(arr[depth],0,-1):
        perm(depth+i,res+1)
    
    
    
for i in range(1,TC+1):
    n, *arr = list(map(int,input().split()))
    cnt = n
    perm(0,0)
    print(f'#{i}', end = " ")
    print(cnt-1)