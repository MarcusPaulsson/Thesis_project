def max_substring_removal(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(s) - j

s = input().strip()
t = input().strip()
print(max_substring_removal(s, t))