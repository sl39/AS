TC = int(input())


def check(b,n):
    ans = 0
    for i in range(len(b)):
        ans += int(b[i]) * (n**(len(b)-i-1))
    return ans 


def two(b2):
    arr = []
    for i in range(len(b2)):
        if b2[i] == "1":
            b2[i] = "0"
            arr.append(check(b2,2))
            b2[i] = "1"
        else:
            b2[i] = "1"
            arr.append(check(b2,2))
            b2[i] = "0"
    return arr


def three(b3):
    global ans2
    for i in range(len(b3)):
        if b3[i] == "0":
            b3[i] = "1"
            if check(b3,3) in ans2:
                return check(b3,3)
            b3[i] = "2"
            if check(b3,3) in ans2:
                return check(b3,3)
            b3[i] = "0"
        elif b3[i] == "1":
            b3[i] = "0"
            if check(b3,3) in ans2:
                return check(b3,3)
            b3[i] = "2"
            if check(b3,3) in ans2:
                return check(b3,3)
            b3[i] = "1"
        
        else:
            b3[i] = "0"
            if check(b3,3) in ans2:
                return check(b3,3)
            b3[i] = "1"
            if check(b3,3) in ans2:
                return check(b3,3)
            b3[i] = "2"






for T in range(1,TC+1):
    b2 = list(input().strip())
    b3 = list(input().strip())
    ans2 = two(b2)
    print(f"#{T}", end =" ")
    print(three(b3))
    