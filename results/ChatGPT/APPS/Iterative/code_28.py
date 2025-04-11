n = int(input())
files = [input().split() for _ in range(n)]

examples = [name for name, type_ in files if type_ == '1']
regulars = [name for name, type_ in files if type_ == '0']

moves = []
# Renaming examples to 1, 2, ..., e
for i, name in enumerate(examples):
    moves.append(f"move {name} {i + 1}")

# Renaming regular tests to e + 1, e + 2, ..., n
for i, name in enumerate(regulars):
    moves.append(f"move {name} {len(examples) + i + 1}")

print(len(moves))
for move in moves:
    print(move)