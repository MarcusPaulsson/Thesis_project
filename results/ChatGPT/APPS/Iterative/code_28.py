n = int(input())
files = [input().split() for _ in range(n)]

examples = [f[0] for f in files if f[1] == '1']
regulars = [f[0] for f in files if f[1] == '0']

moves = []

# Move examples to their new positions
moves.extend(f"move {file} {i + 1}" for i, file in enumerate(examples))

# Move regulars to their new positions
moves.extend(f"move {file} {len(examples) + i + 1}" for i, file in enumerate(regulars))

print(len(moves))
print("\n".join(moves))