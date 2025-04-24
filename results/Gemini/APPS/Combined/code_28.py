def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())

    examples = []
    regular = []
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))

    moves = []
    e = len(examples)

    # Function to find a temporary name that doesn't exist
    def find_temp_name(existing_names):
        temp_name = "temp"
        temp_num = 0
        while True:
            temp_name_full = temp_name + str(temp_num)
            if temp_name_full not in existing_names:
                return temp_name_full
            temp_num += 1

    existing_names = set(file[0] for file in files)

    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            # Find a temporary name
            temp_name = find_temp_name(existing_names)
            existing_names.add(temp_name)

            moves.append(f"move {examples[i][0]} {temp_name}")

            # Find the file that is currently named i+1
            target_file = None
            for j in range(n):
                if files[j][0] == str(i + 1):
                    target_file = files[j][0]
                    break
            
            if target_file:
                # Move the file at i+1 to the original location of the example
                moves.append(f"move {target_file} {examples[i][0]}")
                existing_names.add(examples[i][0])
                existing_names.remove(target_file)
            
            # Move the temporary file to the correct example location
            moves.append(f"move {temp_name} {i + 1}")
            existing_names.add(str(i + 1))
            existing_names.remove(temp_name)

    # Move regular files to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            # Find a temporary name
            temp_name = find_temp_name(existing_names)
            existing_names.add(temp_name)

            moves.append(f"move {regular[i][0]} {temp_name}")

            # Find the file that is currently named e+i+1
            target_file = None
            for j in range(n):
                if files[j][0] == str(e + i + 1):
                    target_file = files[j][0]
                    break
            
            if target_file:
                # Move the file at e+i+1 to the original location of the regular file
                moves.append(f"move {target_file} {regular[i][0]}")
                existing_names.add(regular[i][0])
                existing_names.remove(target_file)

            # Move the temporary file to the correct regular file location
            moves.append(f"move {temp_name} {e + i + 1}")
            existing_names.add(str(e + i + 1))
            existing_names.remove(temp_name)

    print(len(moves))
    for move in moves:
        print(move)

solve()