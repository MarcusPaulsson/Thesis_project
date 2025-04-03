n = int(input())
files = [input().split() for _ in range(n)]

example_files = []
regular_files = []

for name, type_ in files:
    if type_ == '1':
        example_files.append(name)
    else:
        regular_files.append(name)

e = len(example_files)
moves = []

# Move example files to their new names
for i in range(e):
    moves.append(f"move {example_files[i]} {i + 1}")

# Move regular files to their new names
for i in range(len(regular_files)):
    moves.append(f"move {regular_files[i]} {e + i + 1}")

print(len(moves))
for move in moves:
    print(move)