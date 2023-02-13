ls = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]]

visited = [1] * 8
graph = [[] for i in range(8)]
for i in ls:
    graph[i[0]].append(i[1])

# dfs_ls = [1]                              # 재귀함수로 구현
#
# def dfs(x) :
#     visited[x] = 0
#     for i in graph[x]:
#         if visited[i]:
#             dfs_ls.append(i)
#             dfs(i)
# dfs(1)
# print(*dfs_ls)

def def1(x):                                    # pop으로 구현
    lst = []
    stack = [x]
    while stack:
        p = stack.pop()
        if visited[p]:
            visited[p] = 0
            lst.append(p)
            if len(graph[p]):
                for i in range(len(graph[p])-1,-1,-1):
                    stack.append(graph[p][i])
    return lst

print(def1(1))
