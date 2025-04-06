def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def check(d):
        for target in set(a):
            possible = True
            for x in a:
                if x == target:
                    continue
                elif x + d == target:
                    continue
                elif x - d == target:
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