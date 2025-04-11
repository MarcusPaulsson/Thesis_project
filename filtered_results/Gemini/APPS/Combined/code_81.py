def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    strings.sort(key=len)

    def is_substring(a, b):
        return a in b

    def check_order(order):
        for i in range(1, len(order)):
            for j in range(i):
                if not is_substring(order[j], order[i]):
                    return False
        return True

    if check_order(strings):
        print("YES")
        for s in strings:
            print(s)
    else:
        print("NO")

solve()