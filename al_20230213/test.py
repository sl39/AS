ls = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]]

visited = [0] * 8
graph = [[] for i in range(8)]
for i in ls:
    graph[i[0]].append(i[1])

stack = [[1]]
while stack:
    v = stack.pop()
