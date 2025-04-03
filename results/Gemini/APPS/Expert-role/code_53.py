def solve():
    n, s = input().split()
    n = int(n)

    def generate_min_lis(n, s):
        arr = [0] * n
        curr = 1
        for i in range(n):
            if i == 0 or s[i-1] == '>':
                j = i
                while j < n - 1 and s[j] == '<':
                    j += 1
                for k in range(j, i - 1, -1):
                    arr[k] = curr
                    curr += 1
        return arr

    def generate_max_lis(n, s):
        arr = [0] * n
        curr = 1
        for i in range(n):
            if i == 0 or s[i-1] == '<':
                j = i
                while j < n - 1 and s[j] == '>':
                    j += 1
                for k in range(j, i - 1, -1):
                    arr[k] = curr
                    curr += 1
        return arr

    min_arr = generate_min_lis(n, s)
    max_arr = generate_max_lis(n, s)

    print(*min_arr)
    print(*max_arr)


t = int(input())
for _ in range(t):
    solve()