def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def check(d):
        for target in set(a):
            possible = True
            for val in a:
                if val == target or val + d == target or val - d == target:
                    continue
                else:
                    possible = False
                    break
            if possible:
                return True
        return False

    for d in range(101):
        if check(d):
            print(d)
            return
    
    print(-1)

solve()