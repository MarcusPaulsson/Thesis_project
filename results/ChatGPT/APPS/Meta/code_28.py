n = int(input())
files = [input().split() for _ in range(n)]

example_files = []
regular_files = []

for filename, file_type in files:
    if file_type == '1':
        example_files.append(filename)
    else:
        regular_files.append(filename)

total_examples = len(example_files)
total_regulars = len(regular_files)

moves = []

# Move example files to their new names
for i in range(total_examples):
    moves.append(f"move {example_files[i]} {i + 1}")

# Move regular files to their new names
for i in range(total_regulars):
    moves.append(f"move {regular_files[i]} {total_examples + i + 1}")

print(len(moves))
for move in moves:
    print(move)