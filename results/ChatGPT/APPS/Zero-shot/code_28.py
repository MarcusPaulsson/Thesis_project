n = int(input())
files = [input().split() for _ in range(n)]
example_files = [name for name, type_ in files if type_ == '1']
regular_files = [name for name, type_ in files if type_ == '0']

script = []
new_names = {}
e = len(example_files)

# Rename example files to 1, 2, ..., e
for i in range(e):
    original_name = example_files[i]
    new_name = str(i + 1)
    script.append(f"move {original_name} {new_name}")
    new_names[original_name] = new_name

# Rename regular files to e+1, e+2, ..., n
for i in range(len(regular_files)):
    original_name = regular_files[i]
    new_name = str(e + i + 1)
    # We need to move the old name to a new name that doesn't exist yet
    script.append(f"move {original_name} {new_name}")
    new_names[original_name] = new_name

print(len(script))
for line in script:
    print(line)