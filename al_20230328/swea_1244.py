TC = int(input())

def dfs(depth):
    global ans
    if depth == m:
        cnt = "".join(n)
        ans = max(int(cnt),ans)
        return
    
    for i in range(nl):
        for j in range(nl):
            if i!= j:
                n[i] ,n[j] = n[j] , n[i]
                if (*n,depth) in dic:
                    pass
                else:
                    dic[(*n,depth)] = 0
                    dfs(depth+1)
                n[i] ,n[j] = n[j] , n[i]


for T in range(1,TC+1):
    n,m = map(str,input().split())
    ans = 0
    n = list(n)
    m = int(m)
    nl = len(n)
    print(f"#{T}", end=" ")
    dic = {}
    dfs(0)
    print(ans)

