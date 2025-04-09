def solve():
    n = int(input())
    s = input()
    t = input()

    def check(res, s, t):
        for i in range(len(res) - 1):
            sub = res[i:i+2]
            if sub == s or sub == t:
                return False
        return True

    def find_string(n, s, t):
        import itertools
        chars = ['a', 'b', 'c']
        
        possible_strings = []

        for p in itertools.permutations(['a'] * n + ['b'] * n + ['c'] * n):
            res = "".join(p)
            if check(res, s, t):
                possible_strings.append(res)

        if possible_strings:
            return possible_strings[0]
        else:
            return None

    result = find_string(n, s, t)

    if result:
        print("YES")
        print(result)
    else:
        print("NO")

solve()