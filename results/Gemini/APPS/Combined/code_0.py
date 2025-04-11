def solve():
    s = input()
    n = len(s)

    first_bracket = -1
    for i in range(n):
        if s[i] == '[':
            first_bracket = i
            break

    if first_bracket == -1:
        print(-1)
        return

    first_colon = -1
    for i in range(first_bracket + 1, n):
        if s[i] == ':':
            first_colon = i
            break

    if first_colon == -1:
        print(-1)
        return

    last_bracket = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            last_bracket = i
            break

    if last_bracket == -1:
        print(-1)
        return

    last_colon = -1
    for i in range(last_bracket - 1, -1, -1):
        if s[i] == ':':
            last_colon = i
            break
            
    if last_colon == -1:
        print(-1)
        return

    if first_bracket >= first_colon or last_bracket <= last_colon:
        print(-1)
        return

    count = 0
    for i in range(first_colon + 1, last_colon):
        if s[i] == '|':
            count += 1

    print(4 + count)

solve()