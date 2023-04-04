from collections import deque

TC = int(input())

def bfs(n):
    q = deque([n])
    while q:
        p = q.popleft()
        if p == m:
            return
        next = p + 1
        if 0< next <= 1000000:
            if visited[next] > visited[p]+1:
                visited[next] = visited[p]+1
                q.append(next)
        next = p - 1
        if 0< next <= 1000000:
            if visited[next] > visited[p]+1:
                visited[next] = visited[p]+1
                q.append(next)
        next = p *2
        if 0< next <= 1000000:
            if visited[next] > visited[p]+1:
                visited[next] = visited[p]+1
                q.append(next)
        next = p - 10
        if 0< next <= 1000000:
            if visited[next] > visited[p]+1:
                visited[next] = visited[p]+1
                q.append(next)

        

for T in range(1,TC+1):
    n,m = map(int,input().split())
    visited = [1000001] * 1000001
    visited[n] = 0
    bfs(n)
    print(f'#{T}', end=" ")
    print(visited[m])