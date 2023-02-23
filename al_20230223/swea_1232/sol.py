import sys
sys.stdin = open("input.txt")


def postorder(v):
    if int(tree[v][1]):
        left = int(tree[v][1])
        right = int(tree[v][2])
        postorder(left)
        postorder(right)
        if tree[v][0] == "+":
            tree[v][0] = tree[int(tree[v][1])][0] + tree[int(tree[v][2])][0]
        elif tree[v][0] == "*":
            tree[v][0] = tree[int(tree[v][1])][0] * tree[int(tree[v][2])][0]
        elif tree[v][0] == "-":
            tree[v][0] = tree[int(tree[v][1])][0] - tree[int(tree[v][2])][0]
        elif tree[v][0] == "/":
            tree[v][0] = tree[int(tree[v][1])][0] / tree[int(tree[v][2])][0]
    else:
        tree[v][0] = int(tree[v][0])

for T in range(1,11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(1,N+1):
        ls = list(map(str,input().split()))
        if len(ls) == 2:
            ls += ["0","0"]
            tree[int(ls[0])] = ls[1:]
        else:
            tree[int(ls[0])] = ls[1:]

    postorder(1)
    print(f"#{T}", end=" ")
    print(int(tree[1][0]))