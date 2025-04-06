s = input()
n = len(s)
first_bracket = -1
last_bracket = -1
first_colon = -1
last_colon = -1

for i in range(n):
    if s[i] == '[':
        first_bracket = i
        break

if first_bracket == -1:
    print(-1)
    exit()

for i in range(n - 1, -1, -1):
    if s[i] == ']':
        last_bracket = i
        break

if last_bracket == -1:
    print(-1)
    exit()

if first_bracket >= last_bracket:
    print(-1)
    exit()

for i in range(first_bracket + 1, last_bracket):
    if s[i] == ':':
        first_colon = i
        break

if first_colon == -1:
    print(-1)
    exit()

for i in range(last_bracket - 1, first_colon, -1):
    if s[i] == ':':
        last_colon = i
        break

if last_colon == -1:
    print(-1)
    exit()

if first_colon >= last_colon:
    print(-1)
    exit()

count = 0
for i in range(first_colon + 1, last_colon):
    if s[i] == '|':
        count += 1

print(4 + count)