def has_palindrome_subsequence(a):
    n = len(a)
    for i in range(n):
        for j in range(i+2, n):
            if a[i] == a[j]:
                return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if has_palindrome_subsequence(a):
        print("YES")
    else:
        print("NO")