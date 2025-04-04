def max_number(n, a, f):
    max_digit = max(f)
    max_index = f.index(max_digit)
    max_value = int(a.replace(str(max_index), str(max_digit)))
    return max_value

n = int(input())
a = input().strip()
f = list(map(int, input().split()))

print(max_number(n, a, f))