def is_substring(a, b):
    return a in b

def can_reorder(strings):
    strings.sort(key=len)
    for i in range(1, len(strings)):
        if not any(is_substring(strings[i], strings[j]) for j in range(i)):
            return False
    return True

n = int(input())
strings = [input().strip() for _ in range(n)]

if can_reorder(strings):
    print("YES")
    for s in strings:
        print(s)
else:
    print("NO")