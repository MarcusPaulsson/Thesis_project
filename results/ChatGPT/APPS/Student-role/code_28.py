n = int(input())
files = [input().split() for _ in range(n)]

examples = []
regulars = []

for name, type_ in files:
    if type_ == '1':
        examples.append(name)
    else:
        regulars.append(name)

script = []
e = len(examples)

# Rename example files to 1, 2, ..., e
for i in range(e):
    script.append(f"move {examples[i]} {i + 1}")

# Rename regular files to e + 1, e + 2, ..., n
for i in range(len(regulars)):
    script.append(f"move {regulars[i]} {e + i + 1}")

print(len(script))
print("\n".join(script))