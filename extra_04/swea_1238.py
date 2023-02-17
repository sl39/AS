import sys
sys.stdin = open("input.txt")

from collections import deque

for T in range(1,11):
    n,m = map(int,input().split())
    nodes = list(map(int,input().split()))
    mat = [[0]*101 for i in range(101)]
    visited = [0] * 101
    n = len(nodes)//2
    for i in range(n):
        mat[nodes[i*2]][nodes[i*2+1]] = 1
    mxidx = 0
    mxvalue = 0
    q = deque([m])
    while q:
        p = q.popleft()
        for i in range(101):
            if mat[p][i]:
                mat[p][i] = 0
                visited[i] = visited[p] + 1
                for j in range(101):
                    mat[j][i] = 0
                q.append(i)
    mxi = 0
    mxv = max(visited)

    for i in range(101):
        if visited[i] == mxv:
            mxi = i
    print(f"#{T}",mxi)
    