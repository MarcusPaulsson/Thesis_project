def max_accordion_length(s):
    max_length = -1
    for i in range(len(s)):
        if s[i] == '[':
            for j in range(i+1, len(s)):
                if s[j] == ']':
                    for k in range(i+1, j):
                        if s[k] == ':' and s[k+1] == ':' and all(c == '|' for c in s[k+2:j]):
                            max_length = max(max_length, j-i+1)
    return max_length

s = input().strip()
print(max_accordion_length(s))