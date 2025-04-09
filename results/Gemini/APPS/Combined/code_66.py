def solve():
    n, k = map(int, input().split())
    t = input()

    def find_max_overlap(s1, s2):
        for i in range(min(len(s1), len(s2)), 0, -1):
            if s1[-i:] == s2[:i]:
                return i
        return 0

    if k == 1:
        print(t)
        return

    overlap = find_max_overlap(t, t)
    
    result = t + t[overlap:] * (k - 1)
    print(result)

solve()