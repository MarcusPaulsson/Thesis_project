def construct_string(n, k, t):
    if k == 1:
        return t
    else:
        return t + construct_string(n, k - 1, t)

n, k = map(int, input().split())
t = input()
print(construct_string(n, k, t))