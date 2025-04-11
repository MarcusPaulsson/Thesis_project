def can_color_string(n, s):
    last_seen = {}
    for i, char in enumerate(s):
        if char in last_seen:
            if last_seen[char] != i - 1:
                return "NO"
        last_seen[char] = i

    color = ['0'] * n
    for i in range(n):
        if s[i] in last_seen:
            color[i] = '0' if color[i] == '0' else '1'
            last_seen[s[i]] = -1  # Mark as processed

    return "YES\n" + ''.join(color)

n = int(input())
s = input().strip()
result = can_color_string(n, s)
print(result)