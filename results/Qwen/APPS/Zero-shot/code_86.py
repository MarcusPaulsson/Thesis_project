def solve_problems(n, k):
    if n < k or n > k * (2 ** (k - 1)):
        return "NO"
    else:
        a = [1]
        for i in range(1, k):
            a.append(a[-1] * 2)
        remaining = n - sum(a)
        a[-1] += remaining
        return "YES", " ".join(map(str, a))

n, k = map(int, input().split())
result = solve_problems(n, k)
print(result[0])
if result[0] == "YES":
    print(result[1])