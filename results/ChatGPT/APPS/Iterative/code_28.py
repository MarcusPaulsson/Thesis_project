n = int(input())
files = [input().split() for _ in range(n)]

examples = []
regulars = []
for name, type_ in files:
    if type_ == '1':
        examples.append(name)
    else:
        regulars.append(name)

num_examples = len(examples)
num_regulars = len(regulars)

moves = []
# Renaming example files
for i in range(num_examples):
    moves.append(f"move {examples[i]} {i + 1}")

# Renaming regular files
for i in range(num_regulars):
    moves.append(f"move {regulars[i]} {num_examples + i + 1}")

# Output the result
print(len(moves))
print("\n".join(moves))