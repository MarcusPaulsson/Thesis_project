n = int(input())
files = [input().split() for _ in range(n)]
examples = [file[0] for file in files if file[1] == '1']
regulars = [file[0] for file in files if file[1] == '0']

e = len(examples)
moves = []

for i in range(e):
    moves.append(f"move {examples[i]} {i+1}")

for i in range(len(regulars)):
    moves.append(f"move {regulars[i]} {e+i+1}")

print(len(moves))
for move in moves:
    print(move)