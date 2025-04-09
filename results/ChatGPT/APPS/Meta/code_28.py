n = int(input())
files = [input().split() for _ in range(n)]

examples = []
regulars = []

for name, typ in files:
    if typ == '1':
        examples.append(name)
    else:
        regulars.append(name)

moves = []
# Renaming example files
for i in range(len(examples)):
    moves.append(f"move {examples[i]} {i + 1}")

# Renaming regular files
for i in range(len(regulars)):
    moves.append(f"move {regulars[i]} {len(examples) + i + 1}")

print(len(moves))
for move in moves:
    print(move)