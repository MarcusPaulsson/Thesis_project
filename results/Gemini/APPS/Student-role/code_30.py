def solve():
    n = int(input())
    s = input()

    def calculate_operations(target):
        groups = 0
        in_group = False
        for i in range(n):
            if s[i] != target[i % 2]:
                if not in_group:
                    groups += 1
                    in_group = True
            else:
                in_group = False
        return groups

    target1 = ""
    target2 = ""
    for i in range(n):
        if i % 2 == 0:
            target1 += "0"
            target2 += "1"
        else:
            target1 += "1"
            target2 += "0"

    print(min(calculate_operations(target1), calculate_operations(target2)))

t = int(input())
for _ in range(t):
    solve()