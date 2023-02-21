import sys
sys.stdin = open("sample_input.txt")

from collections import deque

TC = int(input())

for T in range(1,TC+1):
    v,e = map(int,input().split())
    mat = [[0]*(v+1) for _ in range(v+1)]

    ### 각 노드들의 간선을 연결되어 있음을 알려주는 mat
    for _ in range(e):
        v1,v2 = map(int,input().split())
        mat[v1][v2] = 1
        mat[v2][v1] = 1



    # s는 시작 노드 g 는 끝 노드
    s, g = map(int,input().split())


    # 각 노드들의 거리를 알게해줌
    arr = [0] *(v+1)


    q = deque([s])
    while q:
        p = q.popleft()
        if p == g:
            break

        for i in range(1,v+1):
            # 만약에 연결되어 있다
            if mat[p][i]:
                
                # 그리고 만약에 값이 없다면 이전값에 +1

                if not arr[i]:
                    arr[i] = arr[p] + 1
                    q.append(i)
                    # q에 i를 넣어주고
            # 그리고 그 위치 값을 출력
    print(f"#{T}",arr[g])
