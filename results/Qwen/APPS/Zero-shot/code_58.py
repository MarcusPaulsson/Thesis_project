def color_array(n, k, a):
    if len(set(a)) < k:
        return "NO"
    else:
        return "YES"

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(color_array(n, k, a))