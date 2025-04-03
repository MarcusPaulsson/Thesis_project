n = int(input())
files = [input().split() for _ in range(n)]

examples = []
regulars = []

for name, type_ in files:
    if type_ == '1':
        examples.append(name)
    else:
        regulars.append(name)

e = len(examples)
script = []

# Rename examples to "1", "2", ..., "e"
for i in range(1, e + 1):
    script.append(f"move {examples[i - 1]} {i}")

# Rename regular tests to "e + 1", "e + 2", ..., "n"
for i in range(1, n - e + 1):
    script.append(f"move {regulars[i - 1]} {e + i}")

print(len(script))
for line in script:
    print(line)