def clean_string(s):
    cleaned = []
    for char in s:
        if cleaned and cleaned[-1] == '1' and char == '0':
            cleaned.pop()  # Remove the '1'
        else:
            cleaned.append(char)
    return ''.join(cleaned)

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    results.append(clean_string(s))

print('\n'.join(results))