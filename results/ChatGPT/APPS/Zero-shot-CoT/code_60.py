def smallest_xor_sum(a, b):
    return (a ^ b)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(smallest_xor_sum(a, b))