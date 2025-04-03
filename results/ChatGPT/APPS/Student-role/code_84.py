def can_color_string(n, s):
    last_seen = {}
    for i, char in enumerate(s):
        if char in last_seen:
            if last_seen[char] % 2 == i % 2:
                return "NO", ""
        last_seen[char] = i
    
    coloring = []
    for i in range(n):
        if s[i] in last_seen:
            coloring.append(str(last_seen[s[i]] % 2))
        else:
            coloring.append('0')
            last_seen[s[i]] = i
    
    return "YES", ''.join(coloring)

n = int(input())
s = input().strip()

result, color_string = can_color_string(n, s)
print(result)
if result == "YES":
    print(color_string)