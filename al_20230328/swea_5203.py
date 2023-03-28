TC = int(input())



def triple(n,ls):
    if ls[n]//3 == 1:
        return 1
    return 0

def runn(n,ls):
    if n == 0:
        if ls[0] and ls[1] and ls[2]:
            return 1
        return 0
    
    if n == 1:
        if ls[0] and ls[1] and ls[2]:
            return 1
        if ls[1] and ls[2] and ls [3]:
            return 1
        return 0
    if ls[n-2] and ls[n-1] and ls[n]:
        return 1
    if ls[n-1] and ls[n] and ls[n+1]:
        return 1
    if ls[n] and ls[n+1] and ls[n+2]:
        return 1
    
    return 0



for T in range(1,TC+1):
    arr = list(map(int,input().split()))
    first = [0]*12
    second = [0]*12
    print(f"#{T}", end=" ")
    for i in range(12):
        if i%2:
            second[arr[i]] += 1
            if runn(arr[i],second):
                print(2)
                break
            if triple(arr[i],second):
                print(2)
                break
        else:
            first[arr[i]] += 1
            if runn(arr[i],first):
                print(1)
                break
            if triple(arr[i],first):
                print(1)
                break
    else:
        print(0)
            