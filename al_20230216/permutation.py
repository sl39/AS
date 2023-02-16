p = list(range(5))
N = len(p)


chosen = [1] * N


def f(i, k, res):
    if i == k:
        print(res)
        return
    for j in range(N):
        if chosen[j]:
            chosen[j] = 0
            f(i+1,k,res+[p[j]])
            chosen[j] = 1

f(0,3,[])
