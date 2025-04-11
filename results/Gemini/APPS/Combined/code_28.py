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

    def find_temp_name(existing_names):
        temp_name = "temp"
        temp_num = 0
        while True:
            temp_candidate = temp_name + str(temp_num)
            if temp_candidate not in existing_names:
                return temp_candidate
            temp_num += 1

    def move_file(source, destination):
        moves.append(f"move {source} {destination}")
        
    def update_file_name(files_list, old_name, new_name):
        for i in range(len(files_list)):
            if files_list[i][0] == old_name:
                files_list[i] = (new_name, files_list[i][1])
                return

    existing_names = {file[0] for file in files}

    # Move examples to 1, 2, ..., e
    for i in range(e):
        target_name = str(i + 1)
        if examples[i][0] != target_name:
            if target_name in existing_names:
                temp = find_temp_name(existing_names)
                move_file(target_name, temp)
                update_file_name(files, target_name, temp)
                existing_names.remove(target_name)
                existing_names.add(temp)
                
                temp2 = find_temp_name(existing_names)
                move_file(examples[i][0], temp2)
                update_file_name(files, examples[i][0], temp2)
                existing_names.remove(examples[i][0])
                existing_names.add(temp2)
                
                move_file(temp2, target_name)
                update_file_name(files, temp2, target_name)
                existing_names.remove(temp2)
                existing_names.add(target_name)
                
                move_file(temp, examples[i][0])
                update_file_name(files, temp, examples[i][0])
                existing_names.remove(temp)
                existing_names.add(examples[i][0])
                
                examples[i] = (target_name, examples[i][1])
                
                for j in range(len(examples)):
                    if examples[j][0] == examples[i][0]:
                        examples[j] = (examples[i][0], examples[j][1])
                        break
            else:
                move_file(examples[i][0], target_name)
                update_file_name(files, examples[i][0], target_name)
                existing_names.remove(examples[i][0])
                existing_names.add(target_name)
                examples[i] = (target_name, examples[i][1])
                

    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        target_name = str(e + i + 1)
        if regular[i][0] != target_name:
            if target_name in existing_names:
                temp = find_temp_name(existing_names)
                move_file(target_name, temp)
                update_file_name(files, target_name, temp)
                existing_names.remove(target_name)
                existing_names.add(temp)
                
                temp2 = find_temp_name(existing_names)
                move_file(regular[i][0], temp2)
                update_file_name(files, regular[i][0], temp2)
                existing_names.remove(regular[i][0])
                existing_names.add(temp2)
                
                move_file(temp2, target_name)
                update_file_name(files, temp2, target_name)
                existing_names.remove(temp2)
                existing_names.add(target_name)
                
                move_file(temp, regular[i][0])
                update_file_name(files, temp, regular[i][0])
                existing_names.remove(temp)
                existing_names.add(regular[i][0])
                
                regular[i] = (target_name, regular[i][1])
                
                for j in range(len(regular)):
                    if regular[j][0] == regular[i][0]:
                        regular[j] = (regular[i][0], regular[j][1])
                        break
            else:
                move_file(regular[i][0], target_name)
                update_file_name(files, regular[i][0], target_name)
                existing_names.remove(regular[i][0])
                existing_names.add(target_name)
                regular[i] = (target_name, regular[i][1])

    print(len(moves))
    for move in moves:
        print(move)

solve()