n = int(input())
files = [input().split() for _ in range(n)]
example_files = []
regular_files = []

for name, typ in files:
    if typ == '1':
        example_files.append(name)
    else:
        regular_files.append(name)

e = len(example_files)
moves = []

# Move example files to 1, 2, ..., e
for i in range(e):
    moves.append(f"move {example_files[i]} {i + 1}")

# Move regular files to e + 1, e + 2, ..., n
for i in range(len(regular_files)):
    moves.append(f"move {regular_files[i]} {e + i + 1}")

print(len(moves))
for move in moves:
    print(move)